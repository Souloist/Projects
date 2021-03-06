import os

# apparently dir is a key word
def create_project_dir(directory):

	# create new directory if one doesnt exist
	if not os.path.exists(directory):
		print("Creating project: " + directory)
		os.makedirs(directory)

def create_data_files(project_name, base_url):

	# queue of webpages that have not been crawled
	queue = project_name + "/queue.txt"

	# list of webpages that have been crawled
	crawled = project_name + "/crawled.txt"

	if not os.path.isfile(queue):

		# make sure queue isnt empty to start otherwise sypder will never crawl
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

# creates new file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)

	# close to prevent data leak
	f.close()

# create_data_files('wikipedia', 'https://wikipedia.org')

# add link data to existing file
def append_to_file(path, data):

	# 'a' means append mode
	with open(path, 'a') as file:
		file.write(data + '\n')

# Delete the contents of a file
def delete_file_contents(path):
	with open(path, 'w'):
		pass

# Convert file contents to set
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as file:
		for line in file:

			# remember to remove the \n at the end of every line
			results.add(line.replace('\n', ''))
	return results

# iterate thru set and place on new line in file
def set_to_file(links, file):
	

	delete_file_contents(file)

	# quality of life improvement
	for link in sorted(links):
		append_to_file(file,link)

