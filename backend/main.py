from data_loader import load_dataset
from data_quality import analyze_data_quality
from statistical_analysis import generate_statistics
from eda import generate_histograms


dataset = load_dataset("data/student_performance.csv")

if dataset is not None:

    print("\nFirst 5 rows:")
    print(dataset.head())

    # Data Quality Analysis
    quality_report = analyze_data_quality(dataset)

    print("\n===== CLOUDLENS DATA QUALITY REPORT =====")

    print(f"Rows: {quality_report['rows']}")
    print(f"Columns: {quality_report['columns']}")

    print("\nMissing Values:")
    print(quality_report["missing_values"])

    print(f"\nDuplicate Rows: {quality_report['duplicate_rows']}")

    print("\nData Types:")
    print(quality_report["data_types"])

    print("\nNumerical Columns:")
    print(quality_report["numerical_columns"])

    print("\nCategorical Columns:")
    print(quality_report["categorical_columns"])

    # Statistical Analysis
    statistics = generate_statistics(dataset)

    print("\n===== CLOUDLENS STATISTICAL ANALYSIS =====")

    for statistic_name, values in statistics.items():
        print(f"\n{statistic_name}:")
        print(values)

        # Statistical Analysis
    statistics = generate_statistics(dataset)

    print("\n===== CLOUDLENS STATISTICAL ANALYSIS =====")

    for statistic_name, values in statistics.items():
        print(f"\n{statistic_name}:")
        print(values)

    # EDA
    generate_histograms(dataset)