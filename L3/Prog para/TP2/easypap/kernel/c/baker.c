#include "easypap.h"

#include <math.h>
#include <omp.h>

void transformation(int i, int j){
    int h = DIM/2;
    int w = DIM/2;
    int rj = j%2;
    int qj = j/2;
    if(i < h) next_img(i,j) = cur_img(2*i+rj, qj);
    else next_img(i,j) = cur_img(4*h-2*i-rj-1, 2*w-qj-1);
}

unsigned baker_compute_seq(unsigned nb_iter)
{
    for (unsigned it = 1; it <= nb_iter; it++)
    {
        for(int i = 0; i < DIM; i++) {
            for(int j = 0; j < DIM; j++){
                 transformation(i, j);
            }
        }
        swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    }
    return 0;
}

unsigned baker_compute_omp(unsigned nb_iter)
{
    for (unsigned it = 1; it <= nb_iter; it++)
    {
        #pragma omp parallel for collapse(2)
        for(int i = 0; i < DIM; i++) {
            for(int j = 0; j < DIM; j++){
                 transformation(i, j);
            }
        }
        swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    }
    return 0;
}

unsigned int baker_do_tile_default(int x, int y, int width, int height){
    for (int i = x; i < x + width; i++)
        for (int j = y; j < y + height; j++)
            transformation(i,j);
    return 0;
}

unsigned baker_compute_tiled(unsigned nb_iter)
{
    for (unsigned it = 1; it <= nb_iter; it++)
    {
        for(int i = 0; i < DIM; i += TILE_W) {
            for(int j = 0; j < DIM; j += TILE_H){
                 do_tile(i, j, TILE_W, TILE_H, 0);
            }
        }
        swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    }
    return 0;
}

unsigned baker_compute_omp_tiled(unsigned nb_iter)
{
    for (unsigned it = 1; it <= nb_iter; it++)
    {
        #pragma omp parallel for collapse(2)
        for(int i = 0; i < DIM; i += TILE_W) {
            for(int j = 0; j < DIM; j += TILE_H){
                 do_tile(i, j, TILE_W, TILE_H, 0);
            }
        }
        swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    }
    return 0;
}

unsigned baker_compute_omp_task(unsigned nb_iter)
{
    #pragma omp parallel
    {
        #pragma omp single nowait
        {
            for (unsigned it = 1; it <= nb_iter; it++)
            {
                for(int i = 0; i < DIM; i++) {
                    for(int j = 0; j < DIM; j++){
                        #pragma omp task untied
                        transformation(i, j);
                    }
                }
                swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
            }
        }
    }
    return 0;
}

unsigned baker_compute_omp_task_tiled(unsigned nb_iter)
{
    for (unsigned it = 1; it <= nb_iter; it++)
    {
        #pragma omp parallel
        for(int i = 0; i < DIM; i += TILE_W) {
            for(int j = 0; j < DIM; j += TILE_H){
                #pragma omp task
                do_tile(i, j, TILE_W, TILE_H, 0);
            }
        }
        swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    }
    return 0;
}

void apply_pixel_cycle(int i, int j, int max_iter) {
    // Trouver la longueur du cycle
    int result_x = i; int result_y = j;
    int cycle_counter = 0;
    int h = DIM/2;
    int w = DIM/2;
    for(int n = 0; n < max_iter; n++){
        if(cycle_counter != 0 && result_x == i && result_y == j) break;
        int rj = result_y%2;
        int qj = result_y/2;
        if(result_x < h) {result_x = 2*result_x+rj; result_y = qj;}
        else {result_x = 4*h-2*result_x-rj-1; result_y =  2*w-qj-1;}
        cycle_counter++;
    }
    result_x = i; result_y = j;
    // Faire l'iteration du cycle
    for(int n = 0; n < max_iter%cycle_counter; n++){
        int rj = result_y%2;
        int qj = result_y/2;
        if(result_x < h) {result_x = 2*result_x+rj; result_y = qj;}
        else {result_x = 4*h-2*result_x-rj-1; result_y =  2*w-qj-1;}
    }
    next_img(i, j) = cur_img(result_x, result_y);
}

unsigned int baker_do_tile_corners(int x, int y, int width, int height){
    for (int i = x; i < x + width; i++)
        for (int j = y; j < y + height; j++)
            apply_pixel_cycle(i,j, max_iter);
    return 0;
}

unsigned baker_compute_corners(unsigned nb_iter)
{
    for(int i = 0; i < DIM; i++) {
        for(int j = 0; j < DIM; j++){
            apply_pixel_cycle(i, j, nb_iter);
        }
    }   
    swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    return 0;
}

unsigned baker_compute_corners_omp(unsigned nb_iter)
{
    #pragma omp parallel for collapse(2)
    for(int i = 0; i < DIM; i++) {
        for(int j = 0; j < DIM; j++){
            apply_pixel_cycle(i, j, nb_iter);
        }
    }   
    swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    return 0;
}

unsigned baker_compute_corners_omp_task(unsigned nb_iter)
{
    #pragma omp parallel
    {
        for(int i = 0; i < DIM; i++) {
            for(int j = 0; j < DIM; j++){
                #pragma omp task
                apply_pixel_cycle(i, j, nb_iter);
            }
        }
    }   
    swap_images(); // fonction de EasyPAP permettant de faire le swap de cur_img et next_img
    return 0;
}

unsigned baker_compute_corners_tiled(unsigned nb_iter)
{
    for(int i = 0; i < DIM; i += TILE_W) {
        for(int j = 0; j < DIM; j += TILE_H){
            do_tile(i, j, TILE_W, TILE_H, 0);
        }
    }
    swap_images();
    return 0;
}

unsigned baker_compute_corners_omp_tiled(unsigned nb_iter)
{
    #pragma omp parallel for collapse(2)
    for(int i = 0; i < DIM; i += TILE_W) {
        for(int j = 0; j < DIM; j += TILE_H){
            do_tile(i, j, TILE_W, TILE_H, 0);
        }
    }
    swap_images();
    return 0;
}

unsigned baker_compute_corners_omp_task_tiled(unsigned nb_iter)
{
    #pragma omp parallel
    for(int i = 0; i < DIM; i += TILE_W) {
        for(int j = 0; j < DIM; j += TILE_H){
            #pragma omp task
            do_tile(i, j, TILE_W, TILE_H, 0);
        }
    }
    swap_images();
    return 0;
}