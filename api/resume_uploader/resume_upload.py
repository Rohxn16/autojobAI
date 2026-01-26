from modules.text_extractor.extract_text import extract_text
from fastapi import (APIRouter,
                     File,
                     UploadFile,
                     HTTPException,
                     status
                    )
from modules.ingestion_pipeline.ingest import (ingest_string_to_vector_database_with_chunking as ingest,
                                               clear_previous_session)
import tempfile

router = APIRouter()

@router.post('/upload_resume')
async def upload_resume(resume: UploadFile = File(...)):
    """
    Endpoint to allow user to upload resume to be stored with vectorization in local database instance

    :param resume -> UploadFile: PDF of the resume
    :return -> str: text extracted from the resume
    """

    #validation check for pdf type
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"File '{resume.filename}' is not a PDF. Please upload a PDF file."
        )

    # save uploaded file into a temporary location
    try:

        # first clear any existing data from the previous session
        clear_previous_session()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix='.pdf',
        ) as temp_file:
            content = await resume.read()
            temp_file.write(content)
            temp_path = temp_file.name

            extracted_text = extract_text(temp_path)

            ingestion = ingest(extracted_text)
            # process the pdf file and store it in a vector db

            print(ingestion)

            return {
                'filename': resume.filename,
                'path': temp_path,
                'extracted_text': extracted_text
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))