from ultralytics import YOLO
import cv2

# ===================== 模型路径（训练完后修改） =====================
model_path = "runs/detect/vegetable_yolov113/weights/best.pt"
# =====================================================================

# 加载训练好的模型
model = YOLO(model_path)


# 识别单张图片函数（给PyQt5调用）
def predict_vegetable(image_path):
    # 推理
    results = model(image_path)

    # 获取结果
    names = model.names
    result_list = []

    for r in results:
        for c in r.boxes.cls:
            class_name = names[int(c)]
            result_list.append(class_name)

    # 去重，返回识别结果
    if len(result_list) > 0:
        final_result = max(set(result_list), key=result_list.count)
    else:
        final_result = "未识别到野菜"

    return final_result


# 测试代码
if __name__ == '__main__':
    test_img = "test.jpg"  # 测试图片路径
    res = predict_vegetable(test_img)
    print("识别结果：", res)