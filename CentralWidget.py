from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSlider
from PySide6.QtCore import QTimer, Signal, QRandomGenerator, Qt
from WidgetChart import WidgetChart


class CentralWidget(QWidget):
    set_temperature = Signal(int)

    def __init__(self, parent):
        super(CentralWidget, self).__init__(parent)

        self.random_generator = QRandomGenerator()
        self.random_generator.seed(42)

        self.temperature_min = -10.0
        self.temperature_max = 40.0

        self.chart_view = WidgetChart(parent)
        self.chart_view.set_temperature_range(self.temperature_min, self.temperature_max)
        self.set_temperature.connect(self.chart_view.add_temperature)

        self.interval = 1000

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(250, 3000)
        self.slider.setValue(self.interval)
        self.slider.valueChanged.connect(self.timer_interval)

        self.push_button_start = QPushButton("Start")
        self.push_button_start.clicked.connect(self.timer_start)

        self.push_button_stop = QPushButton("Stopp")
        self.push_button_stop.clicked.connect(self.timer_stop)

        self.line_edit_min = QLineEdit(str(self.temperature_min))
        self.line_edit_min.textChanged.connect(self.set_temperature_min)

        self.line_edit_max = QLineEdit(str(self.temperature_max))
        self.line_edit_max.textChanged.connect(self.set_temperature_max)

        self.h_box_layout = QHBoxLayout()
        self.h_box_layout.addWidget(self.slider)
        self.h_box_layout.addWidget(self.push_button_start)
        self.h_box_layout.addWidget(self.push_button_stop)
        self.h_box_layout.addWidget(QLabel("Min:"))
        self.h_box_layout.addWidget(self.line_edit_min)
        self.h_box_layout.addWidget(QLabel("Max:"))
        self.h_box_layout.addWidget(self.line_edit_max)

        self.v_box_layout = QVBoxLayout()
        self.v_box_layout.addWidget(self.chart_view)
        self.v_box_layout.addLayout(self.h_box_layout)

        self.setLayout(self.v_box_layout)

        self.timer = QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.timer_timeout)

    def timer_interval(self, value):
        self.interval = value

        self.timer.setInterval(self.interval)

    def timer_start(self):
        self.timer.start(1000)

    def timer_stop(self):
        self.timer.stop()

    def timer_timeout(self):
        scale = 10.0
        range_as_int = int((self.temperature_max - self.temperature_min) * scale)

        random_as_int = self.random_generator.bounded(0, range_as_int)

        random_as_float = float(random_as_int) / scale
        random_as_float += self.temperature_min

        self.set_temperature.emit(random_as_float)

    def set_temperature_min(self, text):
        self.temperature_min = float(text)

        self.chart_view.set_temperature_range(self.temperature_min, self.temperature_max)

    def set_temperature_max(self, text):
        self.temperature_max = float(text)

        self.chart_view.set_temperature_range(self.temperature_min, self.temperature_max)

