#include <iostream>
#include <vector>
#include <array>
#include <fstream>

#if defined(__APPLE__)
#include <OpenGL/gl3.h>
#include <GLUT/glut.h>

#else
#include <GL/glew.h>
#include <GL/glut.h>
#include <GL/freeglut.h>
#endif

#define concat(first, second) first second

#include "Config.h"

#define ENABLE_SHADERS

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>


unsigned int progid;
unsigned int mvpid;

glm::mat4 view;
glm::mat4 proj;
glm::mat4 mvp;

float angle = 0.0f;
float scale = 0.0f;
float inc = 0.1f;

unsigned int vaoids[ 1 ];


std::array< float, 3 > eye = { 0.0f, 0.0f, 5.0f };


void display()
{
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

    // Positionnement de la caméra en ( 0.0f, 0.0f, 5.0f ),
    // on regarde en direction du point ( 0.0f, 0.0f, 0.0f ),
    // la tête est orienté suivant vers le haut l'axe y ( 0.0f, 1.0f, 0.0f ).
    view = glm::lookAt( glm::vec3( eye[ 0 ], eye[ 1 ], eye[ 2 ] ), glm::vec3( 0.0f, 0.0f, 0.0f ), glm::vec3( 0.0f, 1.0f, 0.0f ) );

    // Le repère subit une rotation suivant l'axe z.
    view = glm::rotate( view, glm::degrees( angle ), glm::vec3( 1.0f, 0.0f, 0.0f ) );

    // Calcul de la matrice mvp.
    mvp = proj * view;

    // Passage de la matrice mvp au shader.
    glUniformMatrix4fv( mvpid , 1, GL_FALSE, &mvp[0][0]);

    glBindVertexArray( vaoids[ 0 ] );
    glDrawElements( GL_TRIANGLES, 12, GL_UNSIGNED_SHORT, 0 );

    glutSwapBuffers();
}


void idle()
{
    angle += 0.0001f;
    if( angle >= 360.0f )
    {
        angle = 0.0f;
    }

    if( scale <= 0.0f )
    {
        inc = 0.1f;
    }
    else if( scale > 2.0f )
    {
        inc = -0.1f;
    }

    scale += inc;

    glutPostRedisplay();
}


void reshape( int w, int h )
{
    glViewport(0, 0, w, h);
    // Modification de la matrice de projection à chaque redimensionnement de la fenêtre.
    proj = glm::perspective( 45.0f, w/static_cast< float >( h ), 0.1f, 100.0f );
}


void special( int key, int x, int y )
{
    switch( key )
    {
        case GLUT_KEY_LEFT:
            eye[ 0 ] -= 0.1f;
            break;
        case GLUT_KEY_RIGHT:
            eye[ 0 ] += 0.1f;
            break;
        case GLUT_KEY_UP:
            eye[ 2 ] -= 0.1f;
            break;
        case GLUT_KEY_DOWN:
            eye[ 2 ] += 0.1f;
            break;
    }
    glutPostRedisplay();
}


void initVAOs()
{
    unsigned int vboids[ 4 ];

    std::vector< float > vertices = {
        0.0f,  0.0f,  0.5f,
        -0.5f,  0.5f, -0.5f,
        -0.5f, -0.5f, -0.5f,
        0.5f, -0.5f, -0.5f,
        0.5f,  0.5f, -0.5f
    };

    std::vector< float > colors = {
        1.0f, 0.0f, 0.0f,
        1.0f, 1.0f, 0.0f,
        0.0f, 1.0f, 1.0f,
        1.0f, 0.0f, 1.0f,
        1.0f, 1.0f, 1.0f
    };

    std::vector< unsigned short > indices = {
        0, 1, 2,
        0, 2, 3,
        0, 3, 4,
        0, 4, 1/*,
                1, 3, 2,
                1, 4, 3*/
    };

    std::vector< float > normals( vertices.size() );

    std::fill( std::begin( normals ), std::end( normals ), 0.0f );

    // Calcul des normales.
    for( std::size_t i = 0 ; i < indices.size() ; i+=3 )
    {
        auto x0 = vertices[ 3 * indices [ i ]     ] - vertices[ 3 * indices [ i+1 ]     ];
        auto y0 = vertices[ 3 * indices [ i ] + 1 ] - vertices[ 3 * indices [ i+1 ] + 1 ];
        auto z0 = vertices[ 3 * indices [ i ] + 2 ] - vertices[ 3 * indices [ i+1 ] + 2 ];

        auto x1 = vertices[ 3 * indices [ i ]     ] - vertices[ 3 * indices [ i+2 ]     ];
        auto y1 = vertices[ 3 * indices [ i ] + 1 ] - vertices[ 3 * indices [ i+2 ] + 1 ];
        auto z1 = vertices[ 3 * indices [ i ] + 2 ] - vertices[ 3 * indices [ i+2 ] + 2 ];

        auto x01 = y0 * z1 - y1 * z0;
        auto y01 = z0 * x1 - z1 * x0;
        auto z01 = x0 * y1 - x1 * y0;

        auto norminv = 1.0f / std::sqrt( x01 * x01 + y01 * y01 + z01 * z01 );
        x01 *= norminv;
        y01 *= norminv;
        z01 *= norminv;

        normals[ 3 * indices[ i ]     ] += x01;
        normals[ 3 * indices[ i ] + 1 ] += y01;
        normals[ 3 * indices[ i ] + 2 ] += z01;

        normals[ 3 * indices[ i + 1 ]     ] += x01;
        normals[ 3 * indices[ i + 1 ] + 1 ] += y01;
        normals[ 3 * indices[ i + 1 ] + 2 ] += z01;

        normals[ 3 * indices[ i + 2 ]     ] += x01;
        normals[ 3 * indices[ i + 2 ] + 1 ] += y01;
        normals[ 3 * indices[ i + 2 ] + 2 ] += z01;
    }

    for( std::size_t i = 0 ; i < normals.size() ; i+=3 )
    {
        auto & x = normals[ i     ];
        auto & y = normals[ i + 1 ];
        auto & z = normals[ i + 2 ];

        auto norminv = 1.0f / std::sqrt( x * x + y * y + z * z );

        x *= norminv;
        y *= norminv;
        z *= norminv;
    }


    // Génération d'un Vertex Array Object contenant 3 Vertex Buffer Objects.
    glGenVertexArrays( 1, &vaoids[ 0 ] );
    glBindVertexArray( vaoids[ 0 ] );

    // Génération de 4 VBO.
    glGenBuffers( 4, vboids );

    // VBO contenant les sommets.

    glBindBuffer( GL_ARRAY_BUFFER, vboids[ 0 ] );
    glBufferData( GL_ARRAY_BUFFER, vertices.size() * sizeof( float ), vertices.data(), GL_STATIC_DRAW );

    // L'attribut in_pos du vertex shader est associé aux données de ce VBO.
    auto pos = glGetAttribLocation( progid, "in_pos" );
    glVertexAttribPointer( pos, 3, GL_FLOAT, GL_FALSE, 0, 0 );
    glEnableVertexAttribArray( pos );

    // VBO contenant les couleurs.

    glBindBuffer( GL_ARRAY_BUFFER, vboids[ 1 ] );
    glBufferData( GL_ARRAY_BUFFER, colors.size() * sizeof( float ), colors.data(), GL_STATIC_DRAW );

    // L'attribut in_color du vertex shader est associé aux données de ce VBO.
    auto color = glGetAttribLocation( progid, "in_color" );
    glVertexAttribPointer( color, 3, GL_FLOAT, GL_FALSE, 0, 0 );
    glEnableVertexAttribArray( color );

    // VBO contenant les indices.

    glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, vboids[ 2 ] );
    glBufferData( GL_ELEMENT_ARRAY_BUFFER, indices.size() * sizeof( unsigned short ), indices.data(), GL_STATIC_DRAW );

    // VBO contenant les normales.

    glBindBuffer( GL_ARRAY_BUFFER, vboids[ 3 ] );
    glBufferData( GL_ARRAY_BUFFER, normals.size() * sizeof( float ), normals.data(), GL_STATIC_DRAW );

    auto normal = glGetAttribLocation( progid, "in_normal" );
    glVertexAttribPointer( normal, 3, GL_FLOAT, GL_TRUE, 0, 0 );
    glEnableVertexAttribArray( normal );

    glBindVertexArray( 0 );
}


void initShaders()
{
    unsigned int vsid, fsid;
    int status;
    int logsize;
    std::string log;

    std::ifstream vs_ifs( concat(MY_SHADER_PATH, "/shaders/basic.vert.glsl") );
   std::ifstream fs_ifs( concat(MY_SHADER_PATH, "/shaders/basic.frag.glsl") );


    auto begin = vs_ifs.tellg();
    vs_ifs.seekg( 0, std::ios::end );
    auto end = vs_ifs.tellg();
    vs_ifs.seekg( 0, std::ios::beg );
    auto size = end - begin;

    std::string vs;
    vs.resize( size );
    vs_ifs.read( &vs[ 0 ], size );

    begin = fs_ifs.tellg();
    fs_ifs.seekg( 0, std::ios::end );
    end = fs_ifs.tellg();
    fs_ifs.seekg( 0, std::ios::beg );
    size = end - begin;

    std::string fs;
    fs.resize( size );
    fs_ifs.read( &fs[0], size );

    vsid = glCreateShader( GL_VERTEX_SHADER );
    char const * vs_char = vs.c_str();
    glShaderSource( vsid, 1, &vs_char, nullptr );
    glCompileShader( vsid );

    // Get shader compilation status.
    glGetShaderiv( vsid, GL_COMPILE_STATUS, &status );

    if( !status )
    {
        std::cerr << "Error: vertex shader compilation failed.\n";
        glGetShaderiv( vsid, GL_INFO_LOG_LENGTH, &logsize );
        log.resize( logsize );
        glGetShaderInfoLog( vsid, log.size(), &logsize, &log[0] );
        std::cerr << log << std::endl;
    }

    fsid = glCreateShader( GL_FRAGMENT_SHADER );
    char const * fs_char = fs.c_str();
    glShaderSource( fsid, 1, &fs_char, nullptr );
    glCompileShader( fsid );

    // Get shader compilation status.
    glGetShaderiv( fsid, GL_COMPILE_STATUS, &status );

    if( !status )
    {
        std::cerr << "Error: fragment shader compilation failed.\n";
        glGetShaderiv( fsid, GL_INFO_LOG_LENGTH, &logsize );
        log.resize( logsize );
        glGetShaderInfoLog( fsid, log.size(), &logsize, &log[0] );
        std::cerr << log << std::endl;
    }

    progid = glCreateProgram();

    glAttachShader( progid, vsid );
    glAttachShader( progid, fsid );

    glLinkProgram( progid );

    glUseProgram( progid );

    mvpid = glGetUniformLocation( progid, "mvp" );
}


int main( int argc, char * argv[] )
{
    glutInit( &argc, argv );
#if defined(__APPLE__) && defined(ENABLE_SHADERS)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA|GLUT_3_2_CORE_PROFILE);
#else

glutInitContextVersion( 3, 2 );
//glutInitContextVersion( 4, 5 );
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
    glewInit();
#endif

    glutInitWindowSize( 640, 480 );


    glutCreateWindow( argv[ 0 ]  );

    glutDisplayFunc( display );
    glutReshapeFunc( reshape );
    glutIdleFunc( idle );
    glutSpecialFunc( special );

    // Initialisation de la bibliothèque GLEW.
#if not defined(__APPLE__)
    glewInit();
#endif

    glEnable(GL_DEPTH_TEST);

    initShaders();
    initVAOs();

    glClearColor( 0.0f, 0.0f, 0.0f, 0.0f );

    glutMainLoop();

    return 0;
}
