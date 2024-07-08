import cv2
from s import pyzbar

def decode_qr_codes(frame):
    # Find and decode QR codes
    qr_codes = pyzbar.decode(frame)
    # print("qr_codes", qr_codes)
    for qr_code in qr_codes:
        x, y, w, h = qr_code.rect
        # Draw a rectangle around the QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Get the QR code data
        qr_data = qr_code.data.decode("utf-8")
        qr_type = qr_code.type

        # Draw the QR code data and type on the frame
        text = f"{qr_data} ({qr_type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Decode QR codes in the frame
        frame = decode_qr_codes(frame)

        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()