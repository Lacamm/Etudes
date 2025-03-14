#version 150 core
// version du langage GLSL utilisée, ici 1.5

// mvp est la variable contenant la matrice proj*view*model
// uniform indique que c'est la même matrice pour tous les points
uniform mat4 mvp;

// in indique que la variable est fournie en entrée pour chaque point
// chaque point possède une position 3D
in vec3 in_pos;

out vec3 color;

void main(void)
{
  // calcul de la position du point une fois toutes les transformations appliquées
  gl_Position = mvp * vec4( 2 * in_pos, 1.0 ); // 2* + grand

  if(in_pos.x > 0)
  {
    gl_Position = mvp * vec4 (in_pos + vec3( 1.0, 0.0, 0.0 ), 1.0);
  }
  else 
  {
    gl_Position = mvp * vec4( in_pos, 1.0);
  }

  //color = vec3( 1.0, 1.0, 0.0 );
  //color = vec3( 1.0, 0.0, 0.0 );
  
  //color = vec3(in_pos);
  //color = vec3(in_pos[0],in_pos[0],in_pos[0]);
  color = vec3(gl_Position.x);
}
