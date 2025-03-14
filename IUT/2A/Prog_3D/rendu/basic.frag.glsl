#version 150 core

// couleur émise pour le pixel
in vec4 color;

out vec4 frag_color;

in vec4 lightDir;
in vec4 eyeVec;
in vec4 out_normal;

vec4 toonify(in float intensity) {
    vec4 color;
    if (intensity > 0.98)
    color = vec4(0.8,0.8,0.8,1.0);
    else if (intensity > 0.5)
    color = vec4(0.4,0.4,0.8,1.0); 
    else if (intensity > 0.25)
    color = vec4(0.2,0.2,0.4,1.0);
    else
    color = vec4(0.1,0.1,0.1,1.0);
    return(color);
}


void main( void )
{
    frag_color =  color;
    //frag_color = vec4( mod(ceil(gl_FragCoord.x/30)+ceil(gl_FragCoord.y/10), 2), 0.0, 0.0, 1.0 );
    //frag_color = vec4( pow(cos(gl_FragCoord.x*0.02),2.0), 0.0, 0.0, 1.0 );

    vec4 L = normalize(lightDir);
    vec4 N = normalize(out_normal);

    //frag_color = out_normal;
    float intensity = max(dot(L,N),0.0);
    // frag_color = vec4(intensity,intensity,intensity, 1.0);
    
    //frag_color = toonify(intensity);

    vec4 final_color =vec4(0.34,0.16,0.0, 1.0);
    final_color +=0.6*intensity;

    frag_color = final_color;

    // vec3 E = normalize(eyeVec);
    // vec3 R = reflect(-L, N);
    // float specular = pow(max(dot(R, E), 0.0),2);
    // final_color= vec4(0.8,0.8,0.8,1.0)*specular;
}
