from pydantic import BaseModel, Field, validator

Language_dict={
    "english":"en","german":"de","french":"fr","japanese":"ja","hindi":"hi","italian":"it",
     "korean":"ko","portugue":"pt","russian":"ru","turkish":"tu","chinese":"zh","spanish":"es",
     "polish":"pl"
     }

class InputPrompt(BaseModel):
    data:  str = Field(max_length=256, title="Text Input", description="Text that is converted to speech")
    language : str = Field(title="Output Audio Language",default="english",description="Users can select the list of availabe \
                           languages as the response. Avalibale Langauges are German, Spanish, French, Hindi, Italian, Japanese, Korean, Polish, Portuguese, Russian, Turkish, Chinese")
    
    @validator('data')
    def validate_data_no_null(cls,values):
        values=values.strip()
        if "" == values:
           raise ValueError("Unprocessable Content : Empty Input String.")
        elif len(values) <5:
            raise ValueError("Unprocessable Content : Length of string must be greater then 5.")
        else:
            return values  


    @validator("language")
    def validate_language_from_available(cls,values):
        values=values.lower().strip()
        if "" == values :
           raise ValueError("Unprocessable Content : Language Not Supported.")
        
        elif values in Language_dict.keys():
            lang=Language_dict[values]
            return lang
        else:
            raise ValueError (f"Language '{values}' is not supported. Please check the api docs in SwaggerUi.")