# coding=utf-8

from citasalud.apps.main.models import Especialidad

especialidades = [
    Especialidad(id="00001", nombre="ANESTESIOLOGIA"),
    Especialidad(id="00002", nombre="ANGIOLOGIA"),
    Especialidad(id="00003", nombre="ADMINISTRACION DE HOSPITALES"),
    Especialidad(id="00004", nombre="ANATOMIA PATOLOGICA"),
    Especialidad(id="00005", nombre="ANATOMIA HUMANA"),
    Especialidad(id="00006", nombre="BIOQUIMICA"),
    Especialidad(id="00007", nombre="CIRUGIA TORACICA Y CARDIOVASCULAR"),
    Especialidad(id="00008", nombre="CARDIOLOGIA"),
    Especialidad(id="00009", nombre="CIRUGIA GENERAL"),
    Especialidad(id="00010", nombre="CIRUGIA DE CABEZA Y CUELLO Y MAXILO FACIAL"),
    Especialidad(id="00011", nombre="CIRUGIA PEDIATRICA"),
    Especialidad(id="00012", nombre="CIRUGIA PLASTICA Y REPARADORA"),
    Especialidad(id="00013", nombre="DERMATOLOGIA"),
    Especialidad(id="00014", nombre="ENDOCRINOLOGIA"),
    Especialidad(id="00015", nombre="ENFERMEDADES INFECCIOSAS Y TROPICALES"),
    Especialidad(id="00016", nombre="EMBRIOLOGIA"),
    Especialidad(id="00017", nombre="EPIDEMIOLOGIA"),
    Especialidad(id="00018", nombre="FISIOLOGIA"),
    Especialidad(id="00019", nombre="FARMACOLOGIA"),
    Especialidad(id="00020", nombre="GASTROENTEROLOGIA"),
    Especialidad(id="00021", nombre="GINECOLOGIA Y OBSTETRICIA"),
    Especialidad(id="00022", nombre="GERIATRIA"),
    Especialidad(id="00023", nombre="GENETICA"),
    Especialidad(id="00024", nombre="HEMATOLOGIA"),
    Especialidad(id="00025", nombre="HISTOLOGIA"),
    Especialidad(id="00026", nombre="INMUNOLOGIA Y ALERGIA"),
    Especialidad(id="00027", nombre="MEDICINA NUCLEAR"),
    Especialidad(id="00028", nombre="MEDICINA DEL TRABAJO"),
    Especialidad(id="00029", nombre="MEDICINA INTERNA"),
    Especialidad(id="00030", nombre="MEDICINA LEGAL"),
    Especialidad(id="00031", nombre="MEDICINA FISICA Y REHABILITACION"),
    Especialidad(id="00032", nombre="MEDICINA DEL DEPORTE"),
    Especialidad(id="00033", nombre="NEFROLOGIA"),
    Especialidad(id="00034", nombre="NEUMOLOGIA"),
    Especialidad(id="00035", nombre="NEUROCIRUGIA"),
    Especialidad(id="00036", nombre="NEUROLOGIA"),
    Especialidad(id="00037", nombre="NUTRICION"),
    Especialidad(id="00038", nombre="OFTALMOLOGIA"),
    Especialidad(id="00039", nombre="ONCOLOGIA MEDICA"),
    Especialidad(id="00040", nombre="ONCOLOGIA QUIRURGICA"),
    Especialidad(id="00041", nombre="ORTOPEDIA Y TRAUMATOLOGIA"),
    Especialidad(id="00042", nombre="OTORRINOLARINGOLOGIA"),
    Especialidad(id="00043", nombre="PATOLOGIA CLINICA"),
    Especialidad(id="00044", nombre="PEDIATRIA"),
    Especialidad(id="00045", nombre="PSIQUIATRIA"),
    Especialidad(id="00046", nombre="RADIOLOGIA"),
    Especialidad(id="00047", nombre="RADIOTERAPIA"),
    Especialidad(id="00048", nombre="REUMATOLOGIA"),
    Especialidad(id="00049", nombre="SALUD PUBLICA"),
    Especialidad(id="00050", nombre="UROLOGIA"),
    Especialidad(id="00051", nombre="VENEREOLOGIA"),
    Especialidad(id="00052", nombre="PROCTOLOGIA"),
    Especialidad(id="00053", nombre="MEDICINA INTENSIVA"),
    Especialidad(id="00054", nombre="MEDICINA OCUPACIONAL Y MEDIO AMBIENTE"),
    Especialidad(id="00055", nombre="NEONATOLOGIA"),
    Especialidad(id="00056", nombre="MEDICINA GENERAL INTEGRAL"),
    Especialidad(id="00057", nombre="CIRUGIA GENERAL Y ONCOLOGICA"),
    Especialidad(id="00058", nombre="MEDICINA GENERAL Y ONCOLOGICA"),
    Especialidad(id="00059", nombre="INMUNOLOGIA Y REUMATOLOGIA"),
    Especialidad(id="00060", nombre="NEUMOLOGIA PEDIATRICA"),
    Especialidad(id="00061", nombre="MEDICINA DE EMERGENCIAS Y DESASTRES"),
    Especialidad(id="00062", nombre="ADMINISTRACION DE SALUD"),
    Especialidad(id="00063", nombre="MEDICINA FAMILIAR"),
    Especialidad(id="00064", nombre="RADIODIAGNOSTICO"),
    Especialidad(id="00065", nombre="LABORATORIO CLINICO"),
    Especialidad(id="00066", nombre="NEFROLOGIA PEDIATRICA"),
    Especialidad(id="00067", nombre="UROLOGIA GENERAL Y ONCOLOGICA"),
    Especialidad(id="00068", nombre="PATOLOGIA Y LABORATORIO CLINICO"),
    Especialidad(id="00069", nombre="PARASITOLOGIA"),
    Especialidad(id="00070", nombre="CIRUGIA DE MANO"),
    Especialidad(id="00071", nombre="CIRUGIA NEUMOLOGICA"),
    Especialidad(id="00072", nombre="NEUROLOGIA PEDIATRICA"),
    Especialidad(id="00073", nombre="HISTOPATOLOGIA"),
    Especialidad(id="00074", nombre="ONCOLOGIA PEDIATRICA"),
    Especialidad(id="00075", nombre="MEDICINA INTEGRAL Y GESTION EN SALUD"),
    Especialidad(id="00076", nombre="GINECOLOGIA DE LA NIÑA Y ADOLESCENTE"),
    Especialidad(id="00077", nombre="ANATOMIA PATOLOGICA - PATOLOGIA CLINICA"),
    Especialidad(id="00078", nombre="ANESTESIOLOGIA Y TERAPIA INTENSIVA CARDIOVASCULAR"),
    Especialidad(id="00079", nombre="LABORATORIO CLINICO Y ANATOMIA PATOLOGICA"),
    Especialidad(id="00080", nombre="MEDICINA INTENSIVA PEDIATRICA"),
    Especialidad(id="00081", nombre="ENDOCRINOLOGIA PEDIATRICA Y GENETICA"),
    Especialidad(id="00082", nombre="PSIQUIATRIA INFANTIL"),
    Especialidad(id="00083", nombre="PATOLOGIA ONCOLOGICA"),
    Especialidad(id="00084", nombre="INFECTOLOGIA PEDIATRICA"),
    Especialidad(id="00085", nombre="GINECOLOGIA ONCOLOGICA"),
    Especialidad(id="00086", nombre="GASTROENTEROLOGIA PEDIATRICA"),
    Especialidad(id="00087", nombre="CIRUGIA CARDIOVASCULAR PEDIATRICA"),
    Especialidad(id="00088", nombre="OFTALMOLOGIA ONCOLOGICA"),
    Especialidad(id="00089", nombre="ADOLESCENTOLOGIA"),
    Especialidad(id="00090", nombre="PATOLOGIA"),
    Especialidad(id="00091", nombre="ENDOCRINOLOGIA PEDIATRICA"),
    Especialidad(id="00092", nombre="CIRUGIA ONCOLOGICA DE CABEZA Y CUELLO"),
    Especialidad(id="00094", nombre="CIRUGIA ONCOLOGICA DE MAMAS, TEJIDOS BLANDOS Y PIEL"),
    Especialidad(id="00095", nombre="MEDICINA HIPERBARICA Y SUBACUATICA"),
    Especialidad(id="00097", nombre="CIRUGIA VASCULAR Y ANGIOLOGIA"),
    Especialidad(id="00098", nombre="CIRUGIA GASTROENTEROLOGICA"),
    Especialidad(id="00101", nombre="CIRUGIA ORTOPEDICA Y TRAUMATOLOGIA"),
    Especialidad(id="00104", nombre="CIRUGIA ONCOLOGICA"),
    Especialidad(id="00105", nombre="INMUNOLOGIA CLINICA Y ALERGOLOGIA"),
    Especialidad(id="00106", nombre="OFTALMOLOGIA PEDIATRICA Y ESTRABISMO"),
    Especialidad(id="00107", nombre="DERMATOLOGIA Y VENEREOLOGIA"),
    Especialidad(id="00108", nombre="CARDIOLOGIA INFANTIL"),
    Especialidad(id="10108", nombre="DIAGNOSTICO POR IMAGENES"),
    Especialidad(id="00109", nombre="CIRUGIA DEL APARATO DIGESTIVO"),
    Especialidad(id="00110", nombre="UROLOGIA PEDIATRICA"),
    Especialidad(id="00111", nombre="ANESTESIOLOGIA OBSTETRICA"),
    Especialidad(id="10111", nombre="GESTION EN SALUD"),
    Especialidad(id="00112", nombre="CIRUGIA CARDIOVASCULAR"),
    Especialidad(id="10112", nombre="CIRUGIA PLASTICA Y REPARADORA DE MANO"),
    Especialidad(id="00113", nombre="ANALISIS CLINICOS"),
    Especialidad(id="00114", nombre="EPIDEMIOLOGIA DE CAMPO"),
    Especialidad(id="10114", nombre="ONCOLOGIA RADIOTERAPICA"),
    Especialidad(id="00115", nombre="PEDIATRIA DE EMERGENCIAS Y DESASTRES"),
    Especialidad(id="00116", nombre="RADIOLOGIA INTERVENCIONISTA"),
    Especialidad(id="00117", nombre="ARTROSCOPIA Y CIRUGIA DE RODILLA"),
    Especialidad(id="00118", nombre="TERAPIA INTENSIVA"),
    Especialidad(id="10119", nombre="ALERGOLOGIA"),
    Especialidad(id="00119", nombre="CIRUGIA ONCOLOGICA ABDOMINAL"),
    Especialidad(id="00120", nombre="CIRUGIA CRANEOMAXILOFACIAL"),
    Especialidad(id="00121", nombre="MEDICINA DE REHABILITACION"),
    Especialidad(id="00122", nombre="MEDICINA INTERNA PEDIATRICA"),
    Especialidad(id="00123", nombre="MEDICINA INTERNA - GASTROENTEROLOGIA"),
    Especialidad(id="00124", nombre="HEMATOLOGIA Y HEMOTERAPIA"),
    Especialidad(id="00125", nombre="CIRUGIA, TRANSPLANTOLOGIA Y ANDROLOGIA"),
    Especialidad(id="00126", nombre="NEUROFISIOLOGIA CLINICA"),
    Especialidad(id="00127", nombre="TOXICOLOGIA"),
    Especialidad(id="00128", nombre="RADIOLOGIA E IMAGEN"),
    Especialidad(id="00129", nombre="MEDICINA AEROESPACIAL"),
    Especialidad(id="00130", nombre="HEMATOLOGIA PEDIATRICA"),
    Especialidad(id="10130", nombre="MEDICINA INTENSIVA Y DE EMERGENCIA"),
    Especialidad(id="00131", nombre="HEMATOLOGIA Y HEMOTERAPIA"),
    Especialidad(id="00132", nombre="ANESTESIA, ANALGESIA Y REANIMACION"),
    Especialidad(id="00133", nombre="MEDICINA INTERNA Y PEDIATRIA"),
    Especialidad(id="00134", nombre="ENDOCRINOLOGIA Y NUTRICION"),
    Especialidad(id="00135", nombre="APARATO DIGESTIVO"),
    Especialidad(id="A0001", nombre="DIPLOMATURA EN AUDITORIA MEDICA"),
    Especialidad(id="D0001", nombre="DOCTORADO EN MEDICINA"),
    Especialidad(id="D0002", nombre="DOCTORADO FILOSOFIA MENCION MEDICINA"),
    Especialidad(id="D0003", nombre="DOCTORADO EN BIOQUIMICA Y NUTRICION"),
    Especialidad(id="D0004", nombre="DOCTORADO EN CIRUGIA GENERAL"),
    Especialidad(id="D0005", nombre="DOCTORADO EN CIENCIAS: SALUD PUBLICA"),
    Especialidad(id="D0006", nombre="DOCTORADO EN SALUD PUBLICA"),
    Especialidad(id="D0007", nombre="DOCTORADO EN SALUD PUBLICA AREA DE CONCENTRACION: SALUD MATERNO INFANTIL"),
    Especialidad(id="D0008", nombre="DOCTORADO EN CIENCIAS DE LA SALUD"),
    Especialidad(id="D0009", nombre="DOCTORADO EN MEDICINA Y CIRUGIA"),
    Especialidad(id="D0010", nombre="DOCTORADO EN GESTION EN SALUD"),
    Especialidad(id="D0011", nombre="DOCTORADO EN CIENCIAS"),
    Especialidad(id="M0001", nombre="MAESTRIA EN MEDICINA"),
    Especialidad(id="M0002", nombre="MAESTRIA EN ENFERMEDADES INFECCIOSAS "),
    Especialidad(id="M0003", nombre="MAESTRIA CON MENCION EN NEUMOLOGIA"),
    Especialidad(id="M0004", nombre="MAESTRIA EN OBSTETRICIA CON MENCION EN SALUD REPRODUCTIVA"),
    Especialidad(id="M0005", nombre="MAESTRIA EN GESTION ESTRATEGICA DE LA CALIDAD Y AUDITORIA MEDICA"),
    Especialidad(id="M0006", nombre="MAGISTER EN GOBIERNO Y GERENCIA EN SALUD"),
    Especialidad(id="M0007", nombre="MAESTRIA EN EPIDEMIOLOGIA"),
    Especialidad(id="M0008", nombre="MAESTRIA EN OFTALMOLOGIA"),
    Especialidad(id="M0009", nombre="MAESTRIA EN CIENCIAS: ADMINISTRACION "),
    Especialidad(id="M0010", nombre="MAESTRIA EN SALUD OCUPACIONAL"),
    Especialidad(id="M0011", nombre="MAESTRIA EN SALUD PUBLICA"),
    Especialidad(id="M0012", nombre="MAESTRIA EN GERENCIA DE SERVICIOS DE SALUD"),
    Especialidad(id="M0013", nombre="MAESTRIA EN BIOMEDICAS BASICAS MENCION EN FISIOLOGIA"),
    Especialidad(id="M0014", nombre="MAGISTER EN ECONOMIA Y GESTION DE LA SALUD"),
    Especialidad(id="M0015", nombre="MAGISTER EN SALUD MENTAL DEL NIÑO Y  ADOLESCENTE"),
    Especialidad(id="M0016", nombre="MAESTRIA EN MEDICINA CON MENCION EN GINECOLOGIA Y OBSTETRICIA"),
    Especialidad(id="M0017", nombre="MAESTRIA EN MEDICINA CON MENCION EN PEDIATRIA"),
    Especialidad(id="M0018", nombre="MAESTRIA EN MEDICINA CON MENCION EN CIRUGIA GENERAL"),
    Especialidad(id="M0019", nombre="MAESTRIA EN SALUD PUBLICA CON MENCION EN EPIDEMIOLOGIA"),
    Especialidad(id="M0020", nombre="MAESTRIA EN ADMINISTRACION DE SERVICIOS DE SALUD"),
    Especialidad(id="M0021", nombre="MAESTRIA EN MEDICINA CON MENCION EN GERENCIA EN SALUD"),
    Especialidad(id="M0022", nombre="MAESTRIA EN SALUD PUBLICA CON MENCION PLANIFICACION Y GESTION"),
    Especialidad(id="M0023", nombre="MAGISTER EN GERIATRIA Y GERONTOLOGIA"),
    Especialidad(id="M0024", nombre="MAGISTER EN SALUD PUBLICA CON MENCION EN GESTION DE SERVICIOS DE SALUD"),
    Especialidad(id="M0025", nombre="MAGISTER EN GERENCIA DE SERVICIOS DE SALUD CON MENCION EN SERVICIOS PUBLICOS DE SALUD"),
    Especialidad(id="M0026", nombre="MAESTRIA EN GESTION Y CONDUCCION EN SALUD"),
    Especialidad(id="M0027", nombre="MAESTRIA EN SALUD PUBLICA MENCION PLANIFICACION Y GESTION "),
    Especialidad(id="M0028", nombre="MAGISTER EN DOCENCIA E INVESTIGACION EN SALUD"),
    Especialidad(id="M0029", nombre="MAESTRIA EN CIENCIAS: SALUD PUBLICA CON MENCION EN AUDITORIA MEDICA"),
    Especialidad(id="M0030", nombre="MAESTRIA EN SALUD PUBLICA CON MENCION EN GERENCIA"),
    Especialidad(id="M0031", nombre="MAESTRIA EN CIENCIAS: SALUD PUBLICA CON MENCION DE GERENCIA DE SERVICIOS PUBLICOS"),
    Especialidad(id="M0032", nombre="MAESTRIA EN SALUD PUBLIPA CON MENCION EN GESTION HOSPITALARIA"),
    Especialidad(id="M0033", nombre="MAGISTER EN CIENCIAS EN PLANIFICACION Y FINANZAS EN SALUD"),
    Especialidad(id="M0034", nombre="MAESTRIA EN EFERMEDADES INFECCIOSAS"),
    Especialidad(id="M0035", nombre="MAESTRIA EN MEDICINA CON MENCION EN CIRUGIA PEDIATRICA"),
    Especialidad(id="M0036", nombre="MAESTRIA EN CIENCIAS CON MENCION EN GERENCIA DE SERVICIOS DE SALUD"),
    Especialidad(id="M0037", nombre="MAESTRIA EN FISIOLOGIA"),
    Especialidad(id="M0038", nombre="MAESTRIA EN MEDICINA CON MENCION EN GASTROENTEROLOGIA"),
    Especialidad(id="M0039", nombre="MAESTRIA EN MEDICINA CON MENCION EN CIRUGIA GENERAL Y ONCOLOGICA"),
    Especialidad(id="M0040", nombre="MAESTRIA EN BIOQUIMICA Y NUTRICION"),
    Especialidad(id="M0041", nombre="MAESTRIA EN CIENCIAS DE LA SALUD CON MENCION EN GESTION EN SERVICIOS DE SALUD"),
    Especialidad(id="M0042", nombre="MAESTRIA EN CIENCIAS: ADMINISTRACION Y GESTION EN SALUD"),
    Especialidad(id="M0043", nombre="MAESTRIA EN MEDICINA FAMILIAR, COMUNITARIA Y ATENCION PRIMARIA"),
    Especialidad(id="M0044", nombre="MAESTRIA EN SALUD PUBLICA CON MENCION EN ADMINISTRACION HOSPITALARIA Y DE SERVICIO DE SALUD"),
    Especialidad(id="M0045", nombre="MAESTRIA EN ADMINISTRACION DE EMPRESAS DE SALUD"),
    Especialidad(id="M0046", nombre="MAESTRIA EN MICROBIOLOGIA"),
    Especialidad(id="M0047", nombre="MAESTRIA EN CIENCIAS BASICAS MEDICAS CON MENCION EN FISIOLOGIA"),
    Especialidad(id="M0048", nombre="MAESTRIA EN MEDICINA CON MENCION EN MEDICINA INTERNA"),
    Especialidad(id="M0049", nombre="MAESTRIA EN ATENCION INTEGRAL AL NIÑO"),
    Especialidad(id="M0050", nombre="MAESTRIA EN GESTION Y CONDUCCION EN SALUD"),
    Especialidad(id="M0051", nombre="MAESTRIA EN MEDICINA CON MENCION EN RADIOLOGIA"),
    Especialidad(id="M0052", nombre="MAESTRIA EN SALUD PUBLICA CON MENCION EN SALUD FAMILIAR Y COMUNITARIA"),
    Especialidad(id="M0053", nombre="MAESTRIA EN SALUD PUBLICA CON MENCION EN ADMINISTRACION Y GERENCIA EN LOS SERVICIOS DE SALUD"),
    Especialidad(id="M0054", nombre="MAESTRIA EN URGENCIAS EN ATENCION PRIMARIA"),
    Especialidad(id="M0055", nombre="MAESTRIA EN NEUROCIENCIAS"),
    Especialidad(id="M0056", nombre="MAESTRIA EN PREVENCION DE RIESGOS Y SALUD OCUPACIONAL"),
    Especialidad(id="M0057", nombre="MAESTRIA EN POLITICAS Y PLANIFICACION EN SALUD"),
    Especialidad(id="M0058", nombre="MAESTRIA EN URGENCIAS MEDICAS EN ATENCION PRIMARIA"),
    Especialidad(id="M0059", nombre="MAESTRIA EN CIENCIAS: SALUD PUBLICA CON MENCION EN GERENCIA DE SERVICIOS DE SALUD"),
    Especialidad(id="M0060", nombre="MAESTRIA EN PREVENCION DE RIESGOS Y SALUD OCUPACIONAL, I EDICION"),
    Especialidad(id="M0061", nombre="MAESTRIA EN SALUD LABORAL"),
    Especialidad(id="M0062", nombre="MAESTRIA EN MEDICINA CON MENCION EN CIENCIAS CLINICAS"),
    Especialidad(id="M0063", nombre="MAESTRIA EN DIRECCION Y GESTION DE SERVICIOS DE SALUD"),
    Especialidad(id="M0064", nombre="MAESTRIA EN GESTION DE LOS SERVICIOS DE SALUD"),
    Especialidad(id="M0065", nombre="MAESTRIA EN POLITICAS Y GESTION EN SALUD"),
    Especialidad(id="M0066", nombre="MAESTRIA EN REHABILITACION EN SALUD"),
    Especialidad(id="M0067", nombre="MAESTRIA EN CIENCIAS DE LA SALUD CON MECION EN GESTION EN SERVICIOS DE SALUD"),
    Especialidad(id="M0068", nombre="MAESTRIA EN SALUD OCUPACIONAL Y AMBIENTAL"),
    Especialidad(id="M0069", nombre="MAESTRIA EN INICIACION A LA INVESTIGACION EN MEDICINA"),
    Especialidad(id="M0070", nombre="MAESTRIA EN CIENCIAS BASICAS MEDICAS CON MENCION EN BIOQUIMICA"),
    Especialidad(id="M0071", nombre="MAESTRIA EN NUTRICION CON MENCION EN ASPECTOS BIOLOGICOS DE LA NUTRICION"),
    Especialidad(id="M0072", nombre="MAESTRIA EN CIENCIAS DE LA SALUD"),
    Especialidad(id="M0073", nombre="MAESTRIA EN SALUD PUBLICA MENCION: GERENCIA EN SERVICIOS DE SALUD"),
    Especialidad(id="M0074", nombre="MAESTRIA EN CIENCIAS EN EL PROGRAMA DE SEGURIDAD Y SALUD OCUPACIONAL INTERNACIONAL"),
    Especialidad(id="M0075", nombre="MAESTRIA EN CIENCIAS: AREA DE CONCENTRACION, POLITICAS, PLANIFICACION, GESTION Y PRACTICAS EN SALUD"),
    Especialidad(id="M0076", nombre="MAESTRIA EN FARMACOLOGIA, DESAROLLO, EVALUACION Y UTILIZACION RACIONAL DE MEDICAMENTOS"),
    Especialidad(id="MN001", nombre="MAESTRIA EN CIENCIA CON MENCION UNIVERSITARIA INVESTIGACION EDUCATIVA"),
    Especialidad(id="MN002", nombre="MAESTRIA EN ADMINISTRACION"),
]

Especialidad.objects.bulk_create(especialidades)