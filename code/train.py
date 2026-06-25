from ultralytics import YOLO

# ===================== 【必须修改】你的数据集路径 =====================
dataset_root = "C:\\Users\\15533\\Desktop\\work\\project\\bishe\\2026\\yecai"  # 改成你数据集的文件夹路径
# =====================================================================

# 1. 加载 YOLOv11 预训练模型（n是最轻量版，适合电脑训练）
model = YOLO("yolov11n.pt")

# 2. 开始训练
if __name__ == '__main__':
    model.train(
        data=dataset_root + "/data.yaml",  # 数据集配置
        epochs=30,                       # 训练轮数（100足够毕设）
        imgsz=640,                        # 图片尺寸
        batch=8,                          # 批次大小（电脑卡就改4、2）
        device="cpu",                     # 有N卡就改成 0
        patience=20,                      # 早停，防止过拟合
        save=True,                        # 保存最佳模型
        name="vegetable_yolov11"          # 训练结果保存文件夹名
    )