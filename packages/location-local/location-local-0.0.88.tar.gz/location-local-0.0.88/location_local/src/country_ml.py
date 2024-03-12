from .location_local_constants import LocationLocalConstants
from dotenv import load_dotenv
load_dotenv()
from database_mysql_local.generic_crud_ml import GenericCRUDML   # noqa402
from language_remote.lang_code import LangCode  # noqa: E402
from logger_local.Logger import Logger  # noqa: E402
from user_context_remote.user_context import UserContext  # noqa: E402

logger = Logger.create_logger(
    object=LocationLocalConstants.OBJECT_FOR_LOGGER_CODE)
user_context = UserContext()


class CountryMl(GenericCRUDML):

    def __init__(self):
        logger.start("start init CountryMl")
        GenericCRUDML.__init__(
            self,
            default_schema_name=LocationLocalConstants.LOCATION_SCHEMA_NAME,
            default_table_name=LocationLocalConstants.COUNTRY_TABLE_NAME,
            default_id_column_name=LocationLocalConstants.COUNTRY_ML_ID_COLUMN_NAME)  # noqa501
        logger.end("end init CountryMl")

    def insert(self, country_id: int, country: str, lang_code: LangCode = None,
               title_approved: bool = False):
        logger.start("start insert country_ml",
                     object={'country_id': country_id, 'country': country,
                             'lang_code': lang_code,
                             'title_approved': title_approved})
        LangCode.validate(lang_code)
        lang_code = lang_code or LangCode.detect_lang_code(country)
        country_ml_json = {
                'country_id': country_id,
                'lang_code': lang_code.value,
                'title': country,
                'title_approved': title_approved
        }
        country_ml_id = GenericCRUDML.insert(
            self,
            table_name=LocationLocalConstants.COUNTRY_ML_TABLE_NAME,
            data_json=country_ml_json)
        logger.end("end insert country_ml",
                   object={'country_ml_id': country_ml_id})

        return country_ml_id
