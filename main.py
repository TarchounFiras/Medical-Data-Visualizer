import medical_data_visualizer
from unittest import main

# Run unit tests automatically
main(module='test_module', exit=False)

# Manually call the functions to generate plots
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()
