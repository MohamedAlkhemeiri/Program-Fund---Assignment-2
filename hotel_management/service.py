# service.py
class Service:
    """Represents a service provided by staff."""
    def __init__(self, service_id, service_type, status="pending"):
        self._service_id = service_id
        self._type = service_type
        self._status = status

    def __str__(self):
        return f"Service ID: {self._service_id}, Type: {self._type}, Status: {self._status}"

    # Getters and setters
    def get_service_id(self): return self._service_id
    def set_service_id(self, service_id): self._service_id = service_id
    def get_type(self): return self._type
    def set_type(self, service_type): self._type = service_type
    def get_status(self): return self._status
    def set_status(self, status): self._status = status