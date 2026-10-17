# 来源与使用说明

## 教师课程

- 仓库：https://github.com/zhouxzh/Ascend310
- 课程演示：https://github.com/zhouxzh/Ascend310/tree/main/src/presentation
- 本次检出的代码提交：`2b1c6f509dc9bf12715b65413dd9edebcaffdce2`，原始记录见 `logs/course_commit.txt`。
- 检测和跟踪代码：上述提交的 `samples/case2/`，本仓库不复制整套上游源码。
- `requirements.txt`：直接复制自实际检出的 `samples/case2/requirements.txt`。
- `data/fusion_result.json`：实验时从教师仓库 main 分支 `samples/case1/fusion_result.json` 下载。该次下载未记录提交号，不能将其强行归属于之后检出的代码版本。
- `code/analyze_fusion.py` 与 `code/hello.sh`：依据课程练习目标，在 AI 辅助指导下编写，由学生实际运行。不是教师源码原样复制。

## 模型与视频

- 模型：https://huggingface.co/zhouxzh/SSDLite320 ，文件 `ssd320_mobilenetv3_large_100.onnx`，通过教师下载脚本获得。
- 测试视频：https://github.com/opencv/opencv/blob/4.x/samples/data/vtest.avi ，视频自身不是学生采集的数据。
- 模型与视频的下载版本当时未固定；复现时应记录实际文件校验值，不能保证移动分支始终返回相同文件。
- `evidence/`中的四张JPEG来自学生实际输出视频；PNG为学生提供的真实操作截图。

## 许可边界

第三方代码、数据、模型和测试视频的权利归各自作者，使用时应遵守各来源的许可。本仓库不为第三方材料另行授予许可。教师仓库首页与平台许可证标签曾出现不一致，故不据此给整个成果包统一套用许可证。

## 证据边界

原始日志只保存程序输出，未包含流水线结束后单独执行的 `echo` 输出；退出状态0由终端截图支撑。帧数检查是学生执行的独立验证，证据见截图，不能当作检测程序自动生成的日志。仓库整理阶段写入的说明、表格与复现命令不是新的实测记录。
