## Dialogue and Argumentation Framework
To demonstrate the Dialogue and Argumentation Framework (DAF), it has been bundled with a web-based interface that allows a user to control the selection of dialogue moves provided by the framework. The demonstrator also allows for the editing and creation of dialogue protocols, creation and editing of content for use in dialogues, and the creation and editing of mock coaching variables for testing purposes.

## Build
1. The DAF uses [Docker](https://www.docker.com/), including docker-compose.
2. Download or clone this repository.
3. Open a command line terminal and go to the root folder of the repository
4. Run the command `docker-compose up`. The containers will start to build. This process may take several minutes. During this time, you
may see output in the terminal relating to a `ConnectionRefusedError`; this is normal.
5. When the DAF is ready, the following line will be printed in the terminal `daf_controller | Dialogue and Argumentation Framework ready`.

## Run
1. The `docker-compose up` command also starts the DAF. After the first time installation it should be faster.
2. To test the DAF demonstrator, open a web browser and enter the URL [http://localhost:8080]
3. When the page has loaded, select one of the four options: *Test a protocol*, *Edit protocols*, *Edit content*, or *Edit coaching variables*.

### Test a protocol
1. Select a protocol from the drop-down menu and follow the instructions.
2. After entering the name of the user, you will be presented with a simulation of the dialogue. You can select both the agent and the user moves and examine how the dialogue unfolds and progresses.
### Edit protocols
1. Select a protocol from the drop-down menu, or choose New protocol.
2. Edit or create the protocol and click Save; if you are creating a new protocol, be sure to enter a name in the box.
### Edit content
1. Choose either Edit argument models or Edit dictionary.
2. Create or edit the content when it is displayed in the box.
### Edit coaching variables
The interface to edit coaching variables is provided to allow dialogues to be tested independent of the Knowledge Base. For this
demonstrator, coaching variables are expressed in a JSON object as key-value pairs.
### Stopping
Use ctrl+c to stop the DAF terminal and then the command `docker-compose down` to stop DAF from Docker.

## Troubleshooting

## License
Dialogue and Argumentation Framework (DAF) is licensed under the GNU Lesser General Public License v3.0 (LGPL 3.0).
