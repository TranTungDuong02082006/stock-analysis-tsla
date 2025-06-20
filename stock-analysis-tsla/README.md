# Phân Tích Giá Cổ Phiếu TSLA - Môn Lập Trình Xử Lý Dữ Liệu Với Python

## 🧠 Mục tiêu:
Phân tích biến động giá cổ phiếu của Tesla (TSLA) trong 1 năm gần nhất, từ đó rút ra nhận xét và khuyến nghị đầu tư.

## 🔧 Các bước thực hiện:
- Thu thập dữ liệu từ `yfinance`
- Làm sạch và tiền xử lý dữ liệu
- Tính các chỉ số kỹ thuật: SMA, EMA, RSI
- Phân tích lợi suất, độ biến động
- Trực quan hóa dữ liệu
- Viết báo cáo

## 🗂 Cấu trúc thư mục:
stock-analysis-tsla/
├── data/
│   ├── raw/                  # Dữ liệu gốc lấy từ yfinance
│   │   └── TSLA_stock_data.csv
│   └── processed/            # Dữ liệu đã làm sạch, có thêm cột SMA, RSI,...
│       └── TSLA_clean.csv
│
├── notebooks/
│   └── analysis.ipynb        # Jupyter Notebook chứa toàn bộ quy trình phân tích
│
├── scripts/
│   ├── fetch_data.py         # Script tự động tải và lưu dữ liệu TSLA
│   └── indicators.py         # Hàm tính SMA, EMA, RSI, v.v.
│
├── report/
│   └── report.pdf            # Báo cáo cuối cùng hoặc export từ Notebook
│
├── visuals/
│   ├── close_price_plot.png  # Các biểu đồ để chèn vào báo cáo
│   └── heatmap_corr.png
│
├── README.md                 # Hướng dẫn chạy code và mô tả báo cáo
└── requirements.txt          # Liệt kê thư viện cần cài (yfinance, pandas, seaborn,...)
