from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso

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
  try:
      curso = cursos_dict[curso_id]
      return curso
  except KeyError:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    
  
  
@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def criar_curso(curso: Curso):
      proximo_id = max(cursos_dict.keys()) + 1
      curso.id = proximo_id
      cursos_dict[proximo_id] = curso.dict(exclude={"id"})
      return curso
    
@app.put("/cursos/{curso_id}")
async def editar_curso(curso_id: int, curso: Curso):
    try:
        curso.id = curso_id
        if curso_id in cursos_dict:
            cursos_dict[curso_id] = curso.dict(exclude={"id"})
        else:
            raise KeyError
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_curso(curso_id: int,):
    try:
        del cursos_dict[curso_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)