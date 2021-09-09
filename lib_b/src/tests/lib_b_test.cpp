#include <catch2/catch.hpp>

#include <lib_b/lib_b.h>

SCENARIO( "Basic output test" )
{
  REQUIRE( lum::lib_b::SayHello() == "Hello" );
}
