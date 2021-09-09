#include "lib_b/lib_b.h"

#include "lib_c/lib_c.h"

namespace lum {
namespace lib_b {

std::string SayHello()
{
  return lum::lib_c::SayHello();
}

} // namespace lib_b
} // namespace lum
