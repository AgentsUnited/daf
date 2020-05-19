endpoints = {}

def dgep_endpoint(cmd, required_parameters=None):
    """Decorator to tie methods in the DGEP class to interface endpoints
        Allows for rapid development of new interfaces alongside
        existing REST and ActiveMQ

        :param cmd the endpoint command to map to the DGEP method
        :param required_parameters optional list of required parameters
        :type cmd str
        :type required_parameters list
    """

    if required_parameters is None:
        required_parameters = []
    def wrapper(fn):

        '''Create the new endpoint and add it to the available list'''
        endpoint = {"method": fn.__name__, "parameters": required_parameters}
        endpoints[cmd] = endpoint
        return fn

    return wrapper

def invoke(dgep, cmd, data):
    """Method for invoking an endpoint on the given DGEP instance

        :param dgep DGEP instance to invoke on
        :param cmd the endpoint command to invoke
        :param data data to pass to the endpoint
        :type dgep DGEP
        :type cmd str
        :type data list
    """

    print("INVOKING")

    if cmd in list(endpoints.keys()):
        method = endpoints[cmd]["method"]
        required_parameters = endpoints[cmd]["parameters"]

        ''' Check that all required parameters are present in the data list'''
        if all(elem in data for elem in required_parameters):
            resp = getattr(dgep, method)(data)

            if "extra_data" in data.keys():
                resp["extra_data"] = data["extra_data"]

            if "authToken" in data.keys():
                resp["authToken"] = data["authToken"]

            if "sessionID" in data.keys():
                resp["sessionID"] = data["sessionID"]

            if "dialogueID" in data.keys():
                resp["dialogueID"] = data["dialogueID"]
        else:
            resp = {'error':'insufficient parameters'}
        return resp
    else:
        return {'error': 'No such endpoint'}
