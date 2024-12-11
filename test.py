from ultralytics import RTDETR
model = RTDETR("rtdetr-l.pt")
predict_results = model.predict('https://ultralytics.com/images/bus.jpg', save=True, save_txt=True, save_conf=True, name='mohammed')