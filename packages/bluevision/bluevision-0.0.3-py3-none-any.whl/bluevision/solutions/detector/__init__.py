# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT

from . import models
from bluevision.utils.nms import non_maximum_suppression


class Detector:
    def __init__(self, model, weights=None, nms=None):
        self.model = model
        self.model.set_nms(non_maximum_suppression if nms is None else nms)

        if weights is not None:
            self.load(weights)

    def load(self, weights_path):
        self.model.load(weights_path)

    def __call__(self, image):
        return self.model(image)
