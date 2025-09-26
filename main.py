from fastapi import FastAPI

app = FastAPI()

cursos_dict = {
  1: {"titulo": "Curso de Python", "aulas": 10, "horas": 20},
  2: {"titulo": "Curso de JavaScript", "aulas": 15, "horas": 25},
  3: {"titulo": "Curso de Java", "aulas": 20, "horas": 30} 
}

@app.get("/cursos")
async def listar_cursos():
    return cursos_dict
  
@app.get("/cursos/{curso_id}")
async def obter_curso(curso_id: int):
    curso = cursos_dict[curso_id]
    curso.update({"id": curso_id})
    return curso

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)