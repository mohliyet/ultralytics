from ultralytics import YOLO, RTDETR
# model = YOLO("yolov8n.pt")
model2 = RTDETR("rtdetr-l.pt")
# predict_results = model.predict('https://ultralytics.com/images/bus.jpg')
predict_results2 = model2.predict('https://ultralytics.com/images/bus.jpg')