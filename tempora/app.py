from datetime import datetime
from typing import List, Union
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO)

def parse_time(time_str: str) -> Union[datetime, str]:
    try:
        return datetime.strptime(time_str, '%H:%M')
    except ValueError:
        logging.error(f"Invalid time format: {time_str}")
        return "Invalid time"

def synchronize_clocks(grand_clock_time: str, town_clocks: List[str]) -> List[Union[int, str]]:
    grand_clock = parse_time(grand_clock_time)
    if grand_clock == "Invalid time":
        raise ValueError("Invalid grand clock time format")

    time_differences = []
    for clock_time in town_clocks:
        town_clock = parse_time(clock_time)
        if town_clock != "Invalid time":
            time_difference = int((town_clock - grand_clock).total_seconds() / 60)
            time_differences.append(time_difference)
        else:
            time_differences.append("Invalid time")
    
    return time_differences

def visualize_clocks(grand_clock_time: str, town_clocks: List[str], time_differences: List[Union[int, str]]):
    """
    Visualizes the time differences between the grand clock and town clocks using a horizontal bar chart.

    Args:
        grand_clock_time (str): The time of the grand clock.
        town_clocks (List[str]): A list of town clock names.
        time_differences (List[Union[int, str]]): A list of time differences between the grand clock and town clocks.

    Returns:
        None
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = range(len(town_clocks))
    
    # Generate town names dynamically
    clock_names = [f"Town {i+1}" for i in range(len(town_clocks))]
    
    # Create bars with different colors for valid and invalid times
    colors = ['skyblue' if isinstance(td, int) else 'lightcoral' for td in time_differences]
    bars = ax.barh(y_pos, [td if isinstance(td, int) else 0 for td in time_differences], align='center', color=colors)
    
    # Add text labels
    for i, bar in enumerate(bars):
        if time_differences[i] == "Invalid time":
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, "Invalid time", va='center', ha='left', color='red')
        else:
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f"{time_differences[i]} min", va='center', ha='left')
    
    # Add labels and title
    ax.set_yticks(y_pos)
    ax.set_yticklabels(clock_names)
    ax.set_xlabel('Time Difference (minutes)')
    ax.set_title('Town Clocks Time Differences from Grand Clock')
    
    # Add grid lines
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Add grand clock time at the top
    plt.figtext(0.5, 0.95, f"Grand Clock Time: {grand_clock_time}", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='skyblue', edgecolor='r', label='Valid Time'),
                       Patch(facecolor='lightcoral', edgecolor='r', label='Invalid Time')]
    ax.legend(handles=legend_elements, loc='lower right')
    
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()

# Example usage
if __name__ == "__main__":
    grand_clock_time = '15:00'
    town_clocks = ['14:45', '15:05', '15:00', '14:40', '25:00']
    differences = synchronize_clocks(grand_clock_time, town_clocks)
    print("Time differences:", differences)
    visualize_clocks(grand_clock_time, town_clocks, differences)