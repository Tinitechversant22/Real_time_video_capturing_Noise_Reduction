import cv2

# Function to apply Gaussian Blur
def apply_gaussian_blur(frame):
    return cv2.GaussianBlur(frame, (5, 5), 0)

# Function to apply Median Filtering
def apply_median_filter(frame):
    return cv2.medianBlur(frame, 5)

# Function to apply Bilateral Filtering
def apply_bilateral_filter(frame):
    return cv2.bilateralFilter(frame, 9, 75, 75)

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Apply noise reduction techniques
    gaussian_blur = apply_gaussian_blur(frame)
    median_filter = apply_median_filter(frame)
    bilateral_filter = apply_bilateral_filter(frame)

    # Display the resulting frames
    cv2.imshow('Original', frame)
    cv2.imshow('Gaussian Blur', gaussian_blur)
    cv2.imshow('Median Filter', median_filter)
    cv2.imshow('Bilateral Filter', bilateral_filter)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
