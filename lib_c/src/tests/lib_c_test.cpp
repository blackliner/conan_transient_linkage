#include <catch2/catch.hpp>

#include <lib_c/lib_c.h>

SCENARIO( "Basic output test" )
{
  REQUIRE( lum::lib_c::SayHello() == "Hello" );
}
