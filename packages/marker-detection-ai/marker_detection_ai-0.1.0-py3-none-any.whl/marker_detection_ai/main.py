from ultralytics import YOLO
from importlib.resources import files

def process_image(image_path):

     # Initialize the YOLO model
    weights_path = files('marker_detection_ai').joinpath('best_yolov8m.pt')
    model = YOLO(str(weights_path))
    
    # Run inference
    results = model(image_path)  # results list

    print(f"Images processed. Results returned.")

    # Return the results
    return results

