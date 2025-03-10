import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

def generate_pdf_report(player_1, player_2, csv_file="game_report.csv", output_pdf="tennis_match_report.pdf"):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Compute statistics
    player_1_avg_shot_speed = df[f"Player {player_1} Shot Speed (km/h)"].mean()
    player_2_avg_shot_speed = df[f"Player {player_2} Shot Speed (km/h)"].mean()

    player_1_max_speed = df[f"Player {player_1} Shot Speed (km/h)"].max()
    player_2_max_speed = df[f"Player {player_2} Shot Speed (km/h)"].max()

    # Generate shot speed plot
    plt.figure(figsize=(10, 5))
    plt.plot(df["Frame"], df[f"Player {player_1} Shot Speed (km/h)"], label=f"Player {player_1}", color="blue")
    plt.plot(df["Frame"], df[f"Player {player_2} Shot Speed (km/h)"], label=f"Player {player_2}", color="red")
    plt.xlabel("Frame")
    plt.ylabel("Shot Speed (km/h)")
    plt.title("Shot Speed Over Time")
    plt.legend()
    shot_speed_plot = "shot_speed_plot.png"
    plt.savefig(shot_speed_plot)

    # Generate speed distribution plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df[[f"Player {player_1} Player Speed (km/h)", f"Player {player_2} Player Speed (km/h)"]])
    plt.title("Player Speed Distribution")
    plt.ylabel("Speed (km/h)")
    plt.xticks([0, 1], [f"Player {player_1}", f"Player {player_2}"])
    speed_distribution_plot = "speed_distribution_plot.png"
    plt.savefig(speed_distribution_plot)

    # Create PDF Report
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Tennis Match Analysis Report", ln=True, align="C")

    pdf.ln(10)  # Add space

    # Summary
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Fastest Shot Speed:", ln=True)
    pdf.cell(200, 10, f"- Player {player_1}: {player_1_max_speed:.2f} km/h", ln=True)
    pdf.cell(200, 10, f"- Player {player_2}: {player_2_max_speed:.2f} km/h", ln=True)

    pdf.ln(5)  # Space
    pdf.cell(200, 10, f"Average Shot Speed:", ln=True)
    pdf.cell(200, 10, f"- Player {player_1}: {player_1_avg_shot_speed:.2f} km/h", ln=True)
    pdf.cell(200, 10, f"- Player {player_2}: {player_2_avg_shot_speed:.2f} km/h", ln=True)

    pdf.ln(10)  # Space

    # Add Shot Speed Plot
    pdf.cell(200, 10, "Shot Speed Over Time", ln=True)
    pdf.image(shot_speed_plot, x=10, w=180)

    pdf.ln(10)  # Space

    # Add Speed Distribution Plot
    pdf.cell(200, 10, "Player Speed Distribution", ln=True)
    pdf.image(speed_distribution_plot, x=10, w=180)

    # Save the PDF
    pdf.output(output_pdf)
    print(f"PDF report '{output_pdf}' generated successfully!")

# Generate PDF Report