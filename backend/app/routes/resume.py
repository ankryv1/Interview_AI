from fastapi import APIRouter

router= APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/hello")
def resume():
    return {
        'message': "This is the resume  page"
    }
