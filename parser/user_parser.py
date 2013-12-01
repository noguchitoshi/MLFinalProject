file = "../data/trailhead1000"
i = 1;

def read_in_chunks(file_object, chunk_size=500):
  """Lazy function (generator) to read a file piece by piece.
  Default chunk size: 1k."""
  while True:
      data = file_object.read(chunk_size)
      if not data:
          break
      yield data

# just prints how many entries for each user
file_name = "../data/trailhead20k"
for line in open(file_name):
  a = line.split("\t")
  if (a[1] == 'M'):
    print ("M:" + a[3])
  # print (str(i) + ": " + line)
  # i += 1