from flask import Flask, request, jsonify
import qrcode
import io
import base64
import os
from qr_types import QR_FORMATTERS

app = Flask(__name__)

def generate_qr_code(data_string, size=10):
    """Generate QR code image and return as base64"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(data_string)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64 so it can be sent as JSON
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return img_base64

@app.route('/')
def home():
    """API documentation and examples"""
    pod_name = os.environ.get('HOSTNAME', 'unknown')
    return jsonify({
        "service": "Dynamic QR Code Generator",
        "version": "2.0", # Changed from 1.0
        "pod": pod_name,
        "endpoints": {
            "/generate": "POST - Generate QR code",
            "/health": "GET - Health check"
        },
        "supported_types": list(QR_FORMATTERS.keys()),
        "examples": {
            "url": {
                "type": "url",
                "data": {"url": "https://tutorialsdojo.com"}
            },
            "vcard": {
                "type": "vcard",
                "data": {
                    "name": "Jon Bonso",
                    "phone": "+1234567890",
                    "email": "jon@tutorialsdojo.com",
                    "organization": "Tutorials Dojo"
                }
            },
            "wifi": {
                "type": "wifi",
                "data": {
                    "ssid": "MyNetwork",
                    "password": "MyPassword",
                    "security": "WPA"
                }
            },
            "text": {
                "type": "text",
                "data": {"text": "Hello, Kubernetes!"}
            }
        }
    })

@app.route('/generate', methods=['POST'])
def generate():
    """Generate QR code based on type and data"""
    try:
        request_data = request.get_json()
        
        if not request_data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        qr_type = request_data.get('type', 'text')
        data = request_data.get('data', {})
        size = request_data.get('size', 10)
        
        # Validate type
        if qr_type not in QR_FORMATTERS:
            return jsonify({
                "error": f"Invalid type. Supported: {list(QR_FORMATTERS.keys())}"
            }), 400
        
        # Format data based on type
        formatter = QR_FORMATTERS[qr_type]
        formatted_data = formatter(data)
        
        if not formatted_data:
            return jsonify({"error": "Invalid or empty data"}), 400
        
        # Generate QR code
        qr_image = generate_qr_code(formatted_data, size)
        
        pod_name = os.environ.get('HOSTNAME', 'unknown')
        
        return jsonify({
            "success": True,
            "type": qr_type,
            "qr_code": f"data:image/png;base64,{qr_image}",
            "generated_by_pod": pod_name
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint - Kubernetes uses this"""
    return jsonify({
        "status": "healthy",
        "pod": os.environ.get('HOSTNAME', 'unknown')
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
