#include "lib_a/lib_a.h"

#include "lib_b/lib_b.h"

namespace lum {
namespace lib_a {

std::string SayHello()
{
  return lum::lib_b::SayHello();
}

} // namespace lib_a
} // namespace lum
