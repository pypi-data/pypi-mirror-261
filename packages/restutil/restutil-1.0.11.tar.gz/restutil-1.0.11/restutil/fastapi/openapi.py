

def custom_openapi(app, openapi_schema: dict):
    def wrapper():
        http_methods = ["post", "get", "put", "delete"]
        for method in openapi_schema["paths"]:
            for m in http_methods:
                try:
                    del openapi_schema["paths"][method][m]["responses"]["422"]
                except KeyError:
                    pass
        for schema in list(openapi_schema["components"]["schemas"]):
            if schema in ["HTTPValidationError", "ValidationError"]:
                del openapi_schema["components"]["schemas"][schema]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return wrapper
