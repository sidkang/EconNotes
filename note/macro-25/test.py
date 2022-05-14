# %%
from plantuml import PlantUML
from IPython.display import Image

uml = """@startuml
skinparam defaultTextAlignment center
participant Consumer as con
participant Corp as corp
group Period 1
 [-> con: <latex>L, k_0</latex>
 con -> corp: <math>L,k_0</math>
 corp -> con: <math>w_1L,(1+r_1)k_0</math>
 [<- con: <math>c_1</math>
end
group Period 2
[-> con: <math>L, k_1</math>
con -> corp: <math>L,k_1</math>
corp -> con: <math>w_2L,(1+r_2)k_1</math>
[<- con: <math>c_2</math>
end
@enduml"""

puml = PlantUML('http://www.plantuml.com/plantuml/png/')
Image(url=puml.get_url(uml))
# %%
