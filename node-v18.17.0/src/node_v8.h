#ifndef SRC_NODE_V8_H_
#define SRC_NODE_V8_H_

#if defined(NODE_WANT_INTERNALS) && NODE_WANT_INTERNALS

#include <sstream>
#include "aliased_buffer.h"
#include "base_object.h"
#include "json_utils.h"
#include "node_snapshotable.h"
#include "util.h"
#include "v8.h"

namespace node {
class Environment;
struct InternalFieldInfoBase;

namespace v8_utils {
class BindingData : public SnapshotableObject {
 public:
  BindingData(Realm* realm, v8::Local<v8::Object> obj);

  using InternalFieldInfo = InternalFieldInfoBase;

  SERIALIZABLE_OBJECT_METHODS()
  static constexpr FastStringKey type_name{"node::v8::BindingData"};
  static constexpr EmbedderObjectType type_int =
      EmbedderObjectType::k_v8_binding_data;

  AliasedFloat64Array heap_statistics_buffer;
  AliasedFloat64Array heap_space_statistics_buffer;
  AliasedFloat64Array heap_code_statistics_buffer;

  void MemoryInfo(MemoryTracker* tracker) const override;
  SET_SELF_SIZE(BindingData)
  SET_MEMORY_INFO_NAME(BindingData)
};

class GCProfiler : public BaseObject {
 public:
  enum class GCProfilerState { kInitialized, kStarted, kStopped };
  GCProfiler(Environment* env, v8::Local<v8::Object> object);
  inline ~GCProfiler() override;
  static void New(const v8::FunctionCallbackInfo<v8::Value>& args);
  static void Start(const v8::FunctionCallbackInfo<v8::Value>& args);
  static void Stop(const v8::FunctionCallbackInfo<v8::Value>& args);

  JSONWriter* writer();

  std::ostringstream* out_stream();

  SET_NO_MEMORY_INFO()
  SET_MEMORY_INFO_NAME(GCProfiler)
  SET_SELF_SIZE(GCProfiler)

  uint64_t start_time;
  uint8_t current_gc_type;
  GCProfilerState state;

 private:
  std::ostringstream out_stream_;
  JSONWriter writer_;
};

}  // namespace v8_utils

}  // namespace node

#endif  // defined(NODE_WANT_INTERNALS) && NODE_WANT_INTERNALS

#endif  // SRC_NODE_V8_H_
