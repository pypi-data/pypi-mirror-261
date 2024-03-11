from dataclasses import dataclass


@dataclass
class RelationKey:
    medical_institution_code: str
    medical_record_no: str
    discharge_time: str

    def __repr__(self):
        return '<RelationKey [机构代码：%s， 病案号：%s，出院时间：%s]>' % (self.medical_institution_code, self.medical_record_no, self.discharge_time)

    def __eq__(self, other):
        return self.medical_institution_code == other.medical_institution_code and self.medical_record_no \
               == other.medical_record_no and self.discharge_time == other.discharge_time

    def __hash__(self):
        return hash((self.medical_institution_code, self.medical_record_no, self.discharge_time))