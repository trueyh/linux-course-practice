# 复现说明

以下命令依据学生实际操作整理；本文档本身不是执行日志。推荐使用Ubuntu 22.04、Python 3.10，先进入本成果仓库根目录。

## 基础实验

```bash
chmod 644 code/hello.sh
ls -l code/hello.sh
./code/hello.sh
# 上一步预期Permission denied，属于主动验证。
chmod u+x code/hello.sh
./code/hello.sh
python3 code/analyze_fusion.py
```

统计程序必须从成果仓库根目录运行，预期37项中8项满足条件。原始输出见results目录。

## 取得教师案例

```bash
git clone https://github.com/zhouxzh/Ascend310.git
git -C Ascend310 checkout 2b1c6f509dc9bf12715b65413dd9edebcaffdce2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd Ascend310/samples/case2
python scripts/download_models.py
mkdir -p demo output
```

将OpenCV官方 `vtest.avi` 下载到 `demo/vtest.avi`。下载地址：https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/vtest.avi 。模型默认来源见SOURCES.md。网络失败应先定位下载环节，不代表OpenCV失败。模型、视频的上游分支可能变化，首次复现宜记录SHA256和实际下载日期。

## 检测和跟踪

```bash
python scripts/detection_app.py --device cpu --model models/ssd320_mobilenetv3_large_100.onnx --source demo/vtest.avi --score-threshold 0.35 --no-display --save output/detection_035.mp4
python scripts/detection_app.py --device cpu --model models/ssd320_mobilenetv3_large_100.onnx --source demo/vtest.avi --score-threshold 0.20 --no-display --save output/detection_020.mp4
python scripts/tracking_app.py --device cpu --model models/ssd320_mobilenetv3_large_100.onnx --source demo/vtest.avi --score-threshold 0.35 --track-classes person --no-display --save output/tracking_035.mp4
```

跟踪入口默认可能选NPU，因此显式传入CPU。关闭显示避免依赖图形窗口；输出结束仍需验证视频可读。

## 检查视频并提取图片

在case2目录执行下面代码。将文件名改为检测或跟踪输出，可分别检查。首次检查795帧的结论只适用于本次使用的输入。

```python
import cv2
cap = cv2.VideoCapture("output/tracking_035.mp4")
count = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    count += 1
    if count in (100, 110):
        cv2.imwrite(f"output/tracking_035_frame{count}.jpg", frame)
cap.release()
print("Decoded frames:", count)
```

比较阈值时必须选择同一视频、同一帧。没有完整人工标注时，只能报告观察到的漏检、误检和重复框，不能计算全视频准确率。帧数一致也不等于所有目标检测正确。
