def created(status_code=201, message=""):
    return {
               "status": "success",
               "message": message
           }, status_code
