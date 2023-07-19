import sys
import argparse

from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log

# parse the command line
parser = argparse.ArgumentParser(description="Classify a live camera stream using an image recognition DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=imageNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())

parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--topK", type=int, default=1, help="show the topK number of class predictions (default: 1)")

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the recognition network
net = imageNet(args.network, sys.argv)

# note: to hard-code the paths to load a model, the following API can be used:
#
# net = imageNet(model="model/resnet18.onnx", labels="model/labels.txt", 
#                 input_blob="input_0", output_blob="output_0")


text = ""

def framerate():
    # create video sources & outputs
    input = videoSource(argv=sys.argv)

    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue  

    # classify the image and get the topK predictions
    # if you only want the top class, you can simply run:
    #   class_id, confidence = net.Classify(img)
    predictions = net.Classify(img, topK=args.topK)

    # draw predicted class labels
    for n, (classID, confidence) in enumerate(predictions):
        classLabel = net.GetClassLabel(classID)
        
        return classLabel

while True:
    print("new img taken")

    result = framerate()

    if result == "9": break
    
    text = text + result

print(text)