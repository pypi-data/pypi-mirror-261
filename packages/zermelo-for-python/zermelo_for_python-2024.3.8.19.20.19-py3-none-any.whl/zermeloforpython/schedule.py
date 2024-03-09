from .scheduleitem import scheduleitem
class schedule:
    def __init__(self,json,main) -> None:
        self.session = main
        self.json = json["response"]
        self.status = self.json["status"]
        self.message = self.json["message"]
        self.details = self.json["details"]
        self.eventId = self.json["eventId"]
        self.startRow = self.json["startRow"]
        self.endRow = self.json["endRow"]
        self.totalRows = self.json["totalRows"]
        self.week = self.json["data"][0]["week"]
        self.user = self.json["data"][0]["user"]
        self.appointments = []
        for appointment in self.json["data"][0]["appointments"]:
            self.appointments.append(scheduleitem(appointment,self.session))
    def __repr__(self) -> str:
        return f"schedule(status={self.status},message={self.message},details={self.details},eventId={self.eventId},startRow={self.startRow},endRow={self.endRow},totalRows={self.totalRows},week={self.week},user={self.user})"
    