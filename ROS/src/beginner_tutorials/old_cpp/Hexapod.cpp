#include "HexapodApplication.h"

int main(int argc, char **argv)
{
    // Create application object
    HexapodApplication app;

    try {
        app.go();
    } catch( Exception& e ) {
        fprintf(stderr, "An exception has occurred: %s\n",
                e.what());
    }

    return 0;
}
