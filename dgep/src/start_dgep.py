from interfaces.rest import Rest
from interfaces.activemq import ActiveMQ
from dgep import DGEP
from interfaces.dgep_endpoint import invoke

if __name__ == '__main__':
    print("Starting DGEP 2.0")

    dgep = DGEP()
    dgep.add_interface(Rest())
    dgep.add_interface(ActiveMQ())

    dgep.run()
