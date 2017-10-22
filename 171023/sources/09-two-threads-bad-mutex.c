#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define N 500000
#define M 10000

int data;
void* worker(void* arg __attribute__((unused))) {
    pthread_mutex_t m;
    pthread_mutex_init(&m, NULL);
    for (int i = 0; i < N; i++) {
        pthread_mutex_lock(&m);
        data++;
        pthread_mutex_unlock(&m);
    }
    pthread_mutex_destroy(&m);
    return NULL;
}

int main(void) {
    pthread_t id1, id2;
    assert(pthread_create(&id1, NULL, worker, NULL) == 0);
    assert(pthread_create(&id2, NULL, worker, NULL) == 0);
    for (int i = 0; i < M; i++) {
        int data_snapshot = data;
        if (data_snapshot % 2 == 0) {
            printf("data is %d (in progress)\n", data_snapshot);
            assert(data_snapshot % 2 == 0);
        }
    }
    assert(pthread_join(id1, NULL) == 0);
    assert(pthread_join(id2, NULL) == 0);
    printf("data is %d\n", data);
    return 0;
}
