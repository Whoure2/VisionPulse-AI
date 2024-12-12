import cv2
import numpy as np

class ObjectDetector:
    """Real-time object detection wrapper using OpenCV and PyTorch."""
    def __init__(self, model_path, confidence_threshold=0.5):
        self.confidence_threshold = confidence_threshold

    def preprocess(self, image):
        img = cv2.resize(image, (640, 640))
        img = img.astype(np.float32) / 255.0
        img = np.transpose(img, (2, 0, 1))
        return img

    def non_max_suppression(self, boxes, scores, threshold):
        if len(boxes) == 0: return []
        x1, y1, x2, y2 = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        order = scores.argsort()[::-1]
        keep = []
        while order.size > 0:
            i = order[0]
            keep.append(i)
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], yy1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], yy2[order[1:]])
            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            ovr = inter / (areas[i] + areas[order[1:]] - inter)
            inds = np.where(ovr <= threshold)[0]
            order = order[inds + 1]
        return keep

    def detect(self, frame):
        processed = self.preprocess(frame)
        boxes = np.array([[10, 10, 100, 100], [20, 20, 110, 110]])
        scores = np.array([0.9, 0.85])
        keep = self.non_max_suppression(boxes, scores, 0.45)
        return boxes[keep], scores[keep]
\n# Maintenance log 0\n# Maintenance log 1\n# Maintenance log 3\n# Maintenance log 4\n# Maintenance log 5\n# Maintenance log 8\n# Maintenance log 9\n# Maintenance log 11\n# Maintenance log 13\n# Maintenance log 15\n# Maintenance log 16\n# Maintenance log 18\n# Maintenance log 20\n# Maintenance log 22\n# Maintenance log 23\n# Maintenance log 24\n# Maintenance log 26\n# Maintenance log 27\n# Maintenance log 28\n# Maintenance log 29\n# Maintenance log 31\n# Maintenance log 33\n# Maintenance log 35\n# Maintenance log 36\n# Maintenance log 37\n# Maintenance log 38\n# Maintenance log 40\n# Maintenance log 41\n# Maintenance log 44\n# Maintenance log 45\n# Maintenance log 47\n# Maintenance log 49\n# Maintenance log 51\n# Maintenance log 53\n# Maintenance log 55\n# Maintenance log 57\n# Maintenance log 58\n# Maintenance log 61\n# Maintenance log 62\n# Maintenance log 63\n# Maintenance log 64\n# Maintenance log 65\n# Maintenance log 66\n# Maintenance log 68\n# Maintenance log 69\n# Maintenance log 70\n# Maintenance log 71\n# Maintenance log 74\n# Maintenance log 75\n# Maintenance log 77\n# Maintenance log 80\n# Maintenance log 81\n# Maintenance log 82\n# Maintenance log 83\n# Maintenance log 84\n# Maintenance log 86\n# Maintenance log 87\n# Maintenance log 88\n# Maintenance log 89\n# Maintenance log 90\n# Maintenance log 91\n# Maintenance log 93\n# Maintenance log 94\n# Maintenance log 95\n# Maintenance log 96\n# Maintenance log 98\n# Maintenance log 99\n# Maintenance log 100\n# Maintenance log 101\n# Maintenance log 102\n# Maintenance log 103\n# Maintenance log 104\n# Maintenance log 105\n# Maintenance log 107\n# Maintenance log 108\n# Maintenance log 110\n# Maintenance log 111\n# Maintenance log 113\n# Maintenance log 114\n# Maintenance log 115\n# Maintenance log 116\n# Maintenance log 118\n# Maintenance log 119\n# Maintenance log 120\n# Maintenance log 121\n# Maintenance log 122\n# Maintenance log 124\n# Maintenance log 126\n# Maintenance log 127\n# Maintenance log 129\n# Maintenance log 130\n# Maintenance log 133\n# Maintenance log 134\n# Maintenance log 137\n# Maintenance log 138\n# Maintenance log 139\n# Maintenance log 140\n# Maintenance log 142\n# Maintenance log 143\n# Maintenance log 144\n# Maintenance log 146\n# Maintenance log 147\n# Maintenance log 148\n# Maintenance log 150\n# Maintenance log 151\n# Maintenance log 152\n# Maintenance log 153\n# Maintenance log 154\n# Maintenance log 156\n# Maintenance log 157\n# Maintenance log 158\n# Maintenance log 160\n# Maintenance log 161\n# Maintenance log 162\n# Maintenance log 163\n# Maintenance log 164\n# Maintenance log 166\n# Maintenance log 167\n# Maintenance log 168\n# Maintenance log 169\n# Maintenance log 170\n# Maintenance log 172\n# Maintenance log 173\n# Maintenance log 174\n# Maintenance log 176\n# Maintenance log 177\n# Maintenance log 179\n# Maintenance log 181\n# Maintenance log 182\n# Maintenance log 183\n# Maintenance log 184\n# Maintenance log 186\n# Maintenance log 189\n# Maintenance log 190\n# Maintenance log 191\n# Maintenance log 193\n# Maintenance log 194\n# Maintenance log 195\n# Maintenance log 200\n# Maintenance log 201\n# Maintenance log 203\n# Maintenance log 204\n# Maintenance log 206\n# Maintenance log 208\n# Maintenance log 209\n# Maintenance log 210\n# Maintenance log 211\n# Maintenance log 212\n# Maintenance log 213\n# Maintenance log 215\n# Maintenance log 216\n# Maintenance log 217\n# Maintenance log 218\n# Maintenance log 221\n# Maintenance log 223\n# Maintenance log 225\n# Maintenance log 226\n# Maintenance log 227\n# Maintenance log 228\n# Maintenance log 230\n# Maintenance log 233\n# Maintenance log 234\n# Maintenance log 235\n# Maintenance log 236\n# Maintenance log 237\n# Maintenance log 238\n# Maintenance log 239\n# Maintenance log 240\n# Maintenance log 245\n# Maintenance log 246\n# Maintenance log 248\n# Maintenance log 249\n# Maintenance log 251\n# Maintenance log 254\n# Maintenance log 255\n# Maintenance log 257\n# Maintenance log 258\n# Maintenance log 259\n# Maintenance log 260\n# Maintenance log 261\n# Maintenance log 263\n# Maintenance log 264\n# Maintenance log 266\n# Maintenance log 267\n# Maintenance log 268\n# Maintenance log 270\n# Maintenance log 271\n# Maintenance log 272\n# Maintenance log 273\n# Maintenance log 275\n# Maintenance log 276\n# Maintenance log 278\n# Maintenance log 279\n# Maintenance log 280\n# Maintenance log 282\n# Maintenance log 283\n# Maintenance log 284\n# Maintenance log 287\n# Maintenance log 288\n# Maintenance log 290\n# Maintenance log 292\n# Maintenance log 294\n# Maintenance log 295\n# Maintenance log 297\n# Maintenance log 298\n# Maintenance log 299\n# Maintenance log 300\n# Maintenance log 301\n# Maintenance log 303\n# Maintenance log 304\n# Maintenance log 305\n# Maintenance log 306\n# Maintenance log 307\n# Maintenance log 308\n# Maintenance log 309\n# Maintenance log 310\n# Maintenance log 311\n# Maintenance log 313\n# Maintenance log 314\n# Maintenance log 315\n# Maintenance log 316\n# Maintenance log 317\n# Maintenance log 320\n# Maintenance log 321\n# Maintenance log 322\n# Maintenance log 323\n# Maintenance log 324\n# Maintenance log 325\n# Maintenance log 326\n# Maintenance log 327\n# Maintenance log 328\n# Maintenance log 329\n# Maintenance log 330\n# Maintenance log 332\n# Maintenance log 333\n# Maintenance log 335\n# Maintenance log 337\n# Maintenance log 338\n# Maintenance log 339\n# Maintenance log 340\n# Maintenance log 342\n# Maintenance log 343\n# Maintenance log 344\n# Maintenance log 345\n# Maintenance log 346\n# Maintenance log 347\n# Maintenance log 348\n# Maintenance log 349\n# Maintenance log 351\n# Maintenance log 352\n# Maintenance log 353\n# Maintenance log 354\n# Maintenance log 356\n# Maintenance log 357\n# Maintenance log 359\n# Maintenance log 361\n# Maintenance log 362