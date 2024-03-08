# import pyarrow as pa
#
# s1 = pa.schema(
#    [
#        ('frame', pa.uint32()),
#        ('timestep', pa.uint32()),
#    ]
# )
#
# s2 = pa.schema(
#    [
#        ('x0', pa.float32()),
#        ('y0', pa.float32()),
#        ('z0', pa.float32()),
#        ('lx', pa.float32()),
#        ('ly', pa.float32()),
#        ('lz', pa.float32()),
#        ('alpha', pa.float32()),
#        ('beta', pa.float32()),
#        ('gamma', pa.float32()),
#        ('allow_tilt', pa.bool_()),
#        ('bx', pa.string()),
#        ('by', pa.string()),
#        ('bz', pa.string()),
#    ]
# )
#
# s3 = pa.unify_schemas([s1, s2])
#
# print(s1.names)
