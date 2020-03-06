import docker
import os

spec_directory = "C:\\Users\\tom.rice\\Documents\\Cypress\\Cypress_Project\\cypress\\integration"


def get_spec_files(directory):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(directory):

        for json_file in f:
            if '.spec.js' in json_file:
                if r == spec_directory:
                    files.append(json_file)
                else:
                    full_path = os.path.join(r, json_file)
                    new_path = full_path.split(spec_directory)

                    files.append(new_path[-1].replace('\\', '/'))

    print("Discovered The Following Files To Use As Specs:")
    for f in files:
        print(f)
    print("Number Of Tests Found - {}".format(len(files)))
    return files


local_volume_to_map_to = 'C:\\Users\\tom.rice\\Documents\\Cypress\\Cypress_Project'
desired_containers = 4
counter = 0
client = docker.from_env()
specs = get_spec_files(spec_directory)

while counter < len(specs):
    if len(client.containers.list()) < desired_containers:
        test_name = specs[counter]
        print("Counter {}".format(counter))
        print("Starting Test {}".format(test_name))
        client.containers.run('cypress-tom',
                              remove=True,
                              environment={"testtorun": test_name},
                              detach=True,
                              volumes={local_volume_to_map_to: {'bind': '/e2e', 'mode': 'rw'}}
                              )
        counter += 1



# def delete_all_containers():
#     for container in client.containers.list(all=True):
#         container.stop()
#         container.remove()
#
# delete_all_containers()

