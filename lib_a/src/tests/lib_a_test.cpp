#include <catch2/catch.hpp>

#include <lib_a/lib_a.h>

SCENARIO( "Basic output test" )
{
  REQUIRE( lum::lib_a::SayHello() == "Hello" );
}
