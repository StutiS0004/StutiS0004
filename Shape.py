{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7fda9137",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "def draw_shape(shape):\n",
    "    canvas.delete(\"all\")  # Clear the canvas\n",
    "    if shape == \"Square\":\n",
    "        side_length = int(square_side.get())\n",
    "        color = square_color.get()\n",
    "        canvas.create_rectangle(50, 50, 50 + side_length, 50 + side_length, outline=\"black\", fill=color)\n",
    "    elif shape == \"Rectangle\":\n",
    "        width = int(rectangle_width.get())\n",
    "        height = int(rectangle_height.get())\n",
    "        color = rectangle_color.get()\n",
    "        canvas.create_rectangle(50, 50, 50 + width, 50 + height, outline=\"black\", fill=color)\n",
    "    elif shape == \"Oval\":\n",
    "        width = int(oval_width.get())\n",
    "        height = int(oval_height.get())\n",
    "        color = oval_color.get()\n",
    "        canvas.create_oval(50, 50, 50 + width, 50 + height, outline=\"black\", fill=color)\n",
    "    elif shape == \"Triangle\":\n",
    "        side_length = int(triangle_side.get())\n",
    "        color = triangle_color.get()\n",
    "        canvas.create_polygon(50, 150, 50 + side_length, 50, 50 + side_length * 2, 150, outline=\"black\", fill=color)\n",
    "\n",
    "# Create the main window\n",
    "root = tk.Tk()\n",
    "root.title(\"Shape Drawer\")\n",
    "\n",
    "# Create a canvas to draw shapes\n",
    "canvas = tk.Canvas(root, width=300, height=300)\n",
    "canvas.pack()\n",
    "\n",
    "# Frames for organizing the GUI elements\n",
    "shape_frame = tk.Frame(root)\n",
    "shape_frame.pack()\n",
    "\n",
    "square_frame = tk.Frame(shape_frame)\n",
    "square_frame.pack(side=tk.LEFT)\n",
    "\n",
    "rectangle_frame = tk.Frame(shape_frame)\n",
    "rectangle_frame.pack(side=tk.LEFT)\n",
    "\n",
    "oval_frame = tk.Frame(shape_frame)\n",
    "oval_frame.pack(side=tk.LEFT)\n",
    "\n",
    "triangle_frame = tk.Frame(shape_frame)\n",
    "triangle_frame.pack(side=tk.LEFT)\n",
    "\n",
    "# Function to draw different shapes\n",
    "tk.Label(square_frame, text=\"Square Side Length:\").pack()\n",
    "square_side = tk.Entry(square_frame)\n",
    "square_side.pack()\n",
    "\n",
    "tk.Label(square_frame, text=\"Square Color:\").pack()\n",
    "square_color = tk.Entry(square_frame)\n",
    "square_color.pack()\n",
    "\n",
    "tk.Label(rectangle_frame, text=\"Rectangle Width:\").pack()\n",
    "rectangle_width = tk.Entry(rectangle_frame)\n",
    "rectangle_width.pack()\n",
    "\n",
    "tk.Label(rectangle_frame, text=\"Rectangle Height:\").pack()\n",
    "rectangle_height = tk.Entry(rectangle_frame)\n",
    "rectangle_height.pack()\n",
    "\n",
    "tk.Label(rectangle_frame, text=\"Rectangle Color:\").pack()\n",
    "rectangle_color = tk.Entry(rectangle_frame)\n",
    "rectangle_color.pack()\n",
    "\n",
    "tk.Label(oval_frame, text=\"Oval Width:\").pack()\n",
    "oval_width = tk.Entry(oval_frame)\n",
    "oval_width.pack()\n",
    "\n",
    "tk.Label(oval_frame, text=\"Oval Height:\").pack()\n",
    "oval_height = tk.Entry(oval_frame)\n",
    "oval_height.pack()\n",
    "\n",
    "tk.Label(oval_frame, text=\"Oval Color:\").pack()\n",
    "oval_color = tk.Entry(oval_frame)\n",
    "oval_color.pack()\n",
    "\n",
    "tk.Label(triangle_frame, text=\"Triangle Side Length:\").pack()\n",
    "triangle_side = tk.Entry(triangle_frame)\n",
    "triangle_side.pack()\n",
    "\n",
    "tk.Label(triangle_frame, text=\"Triangle Color:\").pack()\n",
    "triangle_color = tk.Entry(triangle_frame)\n",
    "triangle_color.pack()\n",
    "\n",
    "shape_buttons = [\"Square\", \"Rectangle\", \"Oval\", \"Triangle\"]\n",
    "for shape in shape_buttons:\n",
    "    tk.Button(root, text=shape, command=lambda s=shape: draw_shape(s)).pack()\n",
    "\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08831d32",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
