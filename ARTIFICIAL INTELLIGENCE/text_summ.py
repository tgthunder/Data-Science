import rhino3dm as rh

# Create a new 3D model
model = rh.File3dm()

# Create a box with specified dimensions
box = rh.Box([0, 0, 0], [10, 10, 10])

# Add the box to the model
model.Objects.AddBrep(box.ToBrep())

# Save the model to a 3DM file
model.Write("cube.3dm", rh.File3dmWriteOptions())

print("Cube model has been saved as 'cube.3dm'")
