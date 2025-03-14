#version 150 core
// version du langage GLSL utilisée, ici 4.5

// mvp est la variable contenant la matrice proj*view*model
// uniform indique que c'est la même matrice pour tous les points

uniform mat4 mvp;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;


// in indique que la variable est fournie en entrée pour chaque point
// chaque point possède une position 3D
in vec3 in_pos;

in vec3 eyeVec;

in vec3 in_normal;
out vec4 color;

out vec4 lightDir;
//out vec4 eyeVec;
out vec4 out_normal;


void main(void)
{
  color = vec4(in_normal, 0.0);
  //color =in_pos;

  vec4 normale = model * vec4(in_normal,1.0);
  color = normale*vec4(0.1,0.1,0,0);

  vec4 vVertex = view * model * vec4(in_pos, 1.0);
  //eyeVec = -vVertex;

  vec4 LightSource_position=vec4(10.0,0.0,10.0,0.0);
  lightDir=LightSource_position - vVertex;

  out_normal = model * vec4(in_normal,1.0);


  // calcul de la position du point une fois toutes les transformations appliquées
  
  //gl_Position = mvp * vec4( in_pos, 1.0 );
  gl_Position = proj*view*model * vec4( in_pos, 1.0 );

}


// si la variable eyeVec est décommentée et les lignes ou elle est appelée, le programme renoit un écran noir
// je ne sais pas d'ou ca vient