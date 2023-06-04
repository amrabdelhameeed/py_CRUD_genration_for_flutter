import os

# Function to generate the repository code
def generate_repository_code(word):
    code = f'''
import '../../../../shared_data/web_services/error_handler/api_result.dart';
import '../../../../shared_data/web_services/error_handler/network_exceptions.dart';
import 'package:dio/dio.dart';
import '../../model/{word}_body.dart';
import '../../model/{word}.dart';

import '../web_services/{word}_web_services.dart';

class {word.capitalize()}Repository {{
  final {word.capitalize()}WebServices webServices;

  {word.capitalize()}Repository(this.webServices);

  Future<ApiResult<List<{word.capitalize()}>>> get{word.capitalize()}s({{ int? limit,
     int? page,
     String? sort,}}) async {{
    try {{
      final res = await webServices.get{word.capitalize()}s(
        limit:limit,
        page:page,
        sort:sort
      );
      final {word}s = (res['data']['{word}s'] as List).map((e) => {word.capitalize()}.fromJson(e)).toList()  as List<{word.capitalize()}>;
      return ApiResult.success({word}s);
    }}on DioError catch (e) {{
      return ApiResult.failure(NetworkExceptions.getDioException(e));
    }}
  }}

  Future<ApiResult<{word.capitalize()}>> getOne{word.capitalize()}(int {word}Id) async {{
    try {{
      final res = await webServices.getOne{word.capitalize()}({word}Id);
      final {word} = {word.capitalize()}.fromJson(res['data']['{word}']);
      return ApiResult.success({word});
    }}on DioError catch (e) {{
      return ApiResult.failure(NetworkExceptions.getDioException(e));
    }}
  }}

  Future<ApiResult<{word.capitalize()}>> create{word.capitalize()}({word.capitalize()}Body {word}Body) async {{
    try {{
      final res = await webServices.create{word.capitalize()}({word}Body);
      final new{word.capitalize()} = {word.capitalize()}.fromJson(res['data']['{word}']);
      return ApiResult.success(new{word.capitalize()});
    }}on DioError catch (e) {{
      return ApiResult.failure(NetworkExceptions.getDioException(e));
    }}
  }}

  Future<ApiResult<{word.capitalize()}>> update{word.capitalize()}(int {word}Id, {word.capitalize()}Body {word}Body) async {{
    try {{
      final res = await webServices.update{word.capitalize()}({word}Id, {word}Body);
      final updated{word.capitalize()} = {word.capitalize()}.fromJson(res['data']['{word}']);
      return ApiResult.success(updated{word.capitalize()});
    }}on DioError catch (e) {{
      return ApiResult.failure(NetworkExceptions.getDioException(e));
    }}
  }}

  Future<ApiResult<void>> delete{word.capitalize()}(int {word}Id) async {{
    try {{
      await webServices.delete{word.capitalize()}({word}Id);
      return const ApiResult.success(null);
    }}on DioError catch (e) {{
      return ApiResult.failure(NetworkExceptions.getDioException(e));
    }}
  }}
}}
'''
    return code

# Function to generate the cubit code
def generate_cubit_code(word):
    code = f'''
import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../../shared_data/web_services/error_handler/network_exceptions.dart';
import '../../model/{word}.dart';
import '../../model/{word}_body.dart';
import '../repository/{word}_repository.dart';
import '{word}_state.dart';
class {word.capitalize()}Cubit extends Cubit<{word.capitalize()}State> {{
  final {word.capitalize()}Repository repository;
  List<{word.capitalize()}> {word}s = [];

  {word.capitalize()}Cubit(this.repository) : super(const {word.capitalize()}State.{word}Loading());

  Future<void> get{word.capitalize()}s(
    {{ int? limit,
     int? page,
     String? sort,}}
  ) async {{
    emit(const {word.capitalize()}State.{word}Loading());
    final result = await repository.get{word.capitalize()}s(
    limit:limit,
      page:page,
     sort:sort
    );
    result.when(
      success: ({word}s) {{
        this.{word}s = {word}s;
        emit({word.capitalize()}State.{word}Loaded({word}s));
      }},
      failure: (error) {{
        emit({word.capitalize()}State.{word}Error(NetworkExceptions.getErrorMessage(error)));
      }},
    );
  }}

  Future<void> getOne{word.capitalize()}(int {word}Id) async {{
    emit(const {word.capitalize()}State.{word}Loading());
    final result = await repository.getOne{word.capitalize()}({word}Id);
    result.when(
      success: ({word}) {{
        emit({word.capitalize()}State.getOne{word.capitalize()}({word}));
      }},
      failure: (error) {{
        emit({word.capitalize()}State.{word}Error(NetworkExceptions.getErrorMessage(error)));
      }},
    );
  }}

  Future<void> add{word.capitalize()}({word.capitalize()}Body {word}Body) async {{
    emit(const {word.capitalize()}State.{word}Loading());
    final result = await repository.create{word.capitalize()}({word}Body);
    result.when(
      success: (new{word.capitalize()}) {{
        {word}s.add(new{word.capitalize()});
        emit({word.capitalize()}State.{word}Created(new{word.capitalize()}));
      }},
      failure: (error) {{
        emit({word.capitalize()}State.{word}Error(NetworkExceptions.getErrorMessage(error)));
      }},
    );
  }}

  Future<void> update{word.capitalize()}(int {word}Id, {word.capitalize()}Body {word}Body) async {{
    emit(const {word.capitalize()}State.{word}Loading());
    final result = await repository.update{word.capitalize()}({word}Id, {word}Body);
    result.when(
      success: (updated{word.capitalize()}) {{
        final index = {word}s.indexWhere((d) => d.id == {word}Id);
        {word}s[index] = updated{word.capitalize()};
        emit({word.capitalize()}State.{word}Updated(updated{word.capitalize()}));
      }},
      failure: (error) {{
        emit({word.capitalize()}State.{word}Error(NetworkExceptions.getErrorMessage(error)));
      }},
    );
  }}

  Future<void> delete{word.capitalize()}(int {word}Id) async {{
    emit(const {word.capitalize()}State.{word}Loading());
    final result = await repository.delete{word.capitalize()}({word}Id);
    result.when(
      success: (_) {{
        {word}s.removeWhere((d) => d.id == {word}Id);
        emit({word.capitalize()}State.{word}Deleted({word}Id));
      }},
      failure: (error) {{
        emit({word.capitalize()}State.{word}Error(NetworkExceptions.getErrorMessage(error)));
      }},
    );
  }}
}}
'''
    return code


# Function to generate the cubit state code
def generate_cubit_state_code(word):
    code = f'''
import 'package:freezed_annotation/freezed_annotation.dart';
import '../../model/{word}.dart';
part '{word}_state.freezed.dart';

@freezed
class {word.capitalize()}State with _${word.capitalize()}State {{
  const factory {word.capitalize()}State.{word}Loading() = {word.capitalize()}Loading;
  const factory {word.capitalize()}State.getOne{word.capitalize()}({word.capitalize()} {word}) = GetOne{word.capitalize()};
  const factory {word.capitalize()}State.{word}Created({word.capitalize()} {word}) = {word.capitalize()}Created;
  const factory {word.capitalize()}State.{word}Deleted(int {word}Id) = {word.capitalize()}Deleted;
  const factory {word.capitalize()}State.{word}Updated({word.capitalize()} {word}) = {word.capitalize()}Updated;
  const factory {word.capitalize()}State.{word}Loaded(List<{word.capitalize()}> {word}s) = {word.capitalize()}Loaded;
  const factory {word.capitalize()}State.{word}Error(String errorMessage) = {word.capitalize()}Error;
}}
'''
    return code

# Function to generate the web services code


def generate_web_services_code(word):
    code = f'''
import 'package:dio/dio.dart';
import '../../../../shared_data/core/app_endpoints.dart';
import '../../model/{word}_body.dart';
import 'package:retrofit/retrofit.dart';

part "{word}_web_services.g.dart";

@RestApi(baseUrl: AppEndPoints.baseUrl)
abstract class {word.capitalize()}WebServices {{
  factory {word.capitalize()}WebServices(Dio dio, {{String? baseUrl}}) = _{word.capitalize()}WebServices;

  @GET(AppEndPoints.{word}s)
  Future get{word.capitalize()}s({{
    @Query("limit") int? limit,
    @Query("page") int? page,
    @Query("sort") String? sort,
  }});

  @GET('${{AppEndPoints.{word}s}}/{{{word}Id}}')
  Future getOne{word.capitalize()}(@Path("{word}Id") int {word}Id);

  @POST(AppEndPoints.{word}s)
  Future create{word.capitalize()}(@Body() {word.capitalize()}Body {word}Body);

  @PATCH('${{AppEndPoints.{word}s}}/{{{word}Id}}')
  Future update{word.capitalize()}(
    @Path("{word}Id") int {word}Id,
    @Body() {word.capitalize()}Body {word}Body,
  );

  @DELETE('${{AppEndPoints.{word}s}}/{{{word}Id}}')
  Future<void> delete{word.capitalize()}(@Path("{word}Id") int {word}Id);

}}
'''
    return code


def generate_flutter_screen(word):
    screen_code = f'''
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../data/controller/{word}_cubit.dart';
import '../../data/controller/{word}_state.dart';
final _{word}Cubit = getIt<{word.capitalize()}Cubit>();
class {word.capitalize()}sScreen extends StatelessWidget {{
  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: Text('{word.capitalize()}s'),
      ),
      body: BlocBuilder<{word.capitalize()}Cubit, {word.capitalize()}State>(
        builder: (context, state) {{
          return state.maybeWhen(
            orElse: () {{
              return SizedBox.shrink();
            }},
            {word}Loading: () => Center(child: CircularProgressIndicator()),
            {word}Loaded: ({word}s) {{
              return ListView.builder(
                itemCount: {word}s.length,
                itemBuilder: (context, index) {{
                  final {word} = {word}s[index];
                  return ListTile(
                    title: Text({word}.name),
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        IconButton(
                          icon: Icon(Icons.edit),
                          onPressed: () {{
                            _edit{word.capitalize()}(context, {word});
                          }},
                        ),
                        IconButton(
                          icon: Icon(Icons.delete),
                          onPressed: () {{
                            _delete{word.capitalize()}(context, {word}.id);
                          }},
                        ),
                      ],
                    ),
                  );
                }},
              );
            }},
            {word}Error: (message) => Center(child: Text('Failed to load {word}s')),
          );
        }},
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {{
          _add{word.capitalize()}(context);
        }},
        child: Icon(Icons.add),
      ),
    );
  }}

  void _add{word.capitalize()}(BuildContext context) {{
    showDialog(
      context: context,
      builder: (context) {{
        final _formKey = GlobalKey<FormState>();
        String? {word}Name;

        return AlertDialog(
          title: Text('Add {word.capitalize()}'),
          content: Form(
            key: _formKey,
            child: TextFormField(
              validator: (value) {{
                if (value == null || value.isEmpty) {{
                  return '{word.capitalize()} name cannot be empty';
                }}
                return null;
              }},
              decoration: InputDecoration(
                labelText: '{word.capitalize()} Name',
              ),
              onSaved: (value) {{
                _{word}Cubit.add{word.capitalize()}({word.capitalize()}Body(name: value!));
              }},
            ),
          ),
          actions: [
            TextButton(
              onPressed: () {{
                Navigator.pop(context);
              }},
              child: Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () {{
                if (_formKey.currentState!.validate()) {{
                  _formKey.currentState!.save();
                  Navigator.pop(context);
                }}
              }},
              child: Text('Save'),
            ),
          ],
        );
      }},
    );
  }}

  void _edit{word.capitalize()}(BuildContext context, {word.capitalize()} {word}) {{
    showDialog(
      context: context,
      builder: (context) {{
        final _formKey = GlobalKey<FormState>();
        String? {word}Name = {word}.name;

        return AlertDialog(
          title: Text('Edit {word.capitalize()}'),
          content: Form(
            key: _formKey,
            child: TextFormField(
              initialValue: {word}Name,
              validator: (value) {{
                if (value == null || value.isEmpty) {{
                  return '{word.capitalize()} name cannot be empty';
                }}
                return null;
              }},
              decoration: InputDecoration(
                labelText: '{word.capitalize()} Name',
              ),
              onSaved: (value) {{
                _{word}Cubit.update{word.capitalize()}({word}.id, {word.capitalize()}Body( name: value!));
              }},
            ),
          ),
          actions: [
            TextButton(
              onPressed: () {{
                Navigator.pop(context);
              }},
              child: Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () {{
                if (_formKey.currentState!.validate()) {{
                  _formKey.currentState!.save();
                  Navigator.pop(context);
                }}
              }},
              child: Text('Save'),
            ),
          ],
        );
      }},
    );
  }}

  void _delete{word.capitalize()}(BuildContext context, int {word}Id) {{
    showDialog(
      context: context,
      builder: (context) {{
        return AlertDialog(
          title: Text('Delete {word.capitalize()}'),
          content: Text('Are you sure you want to delete this {word}?'),
          actions: [
            TextButton(
              onPressed: () {{
                Navigator.pop(context);
              }},
              child: Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () {{
                _{word}Cubit.delete{word.capitalize()}({word}Id);
                Navigator.pop(context);
              }},
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all(Colors.red),
              ),
              child: Text('Delete'),
            ),
          ],
        );
      }},
    );
  }}
}}
'''

    return screen_code

# Main function
def main():
    word = input("Enter the word for CRUD operations: ")

    # Create the directories
    if not os.path.exists(word):
        os.makedirs(word)
    
    # Create the model directory
    model_dir = os.path.join(word, "model")
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    # Create the model files
    model_file_path = os.path.join(model_dir, f"{word}.dart")
    if not os.path.exists(model_file_path):
        with open(model_file_path, "w") as file:
            file.write(f"""
import 'package:freezed_annotation/freezed_annotation.dart';
part '{word}.g.dart';
part '{word}.freezed.dart';
@freezed
class {word.capitalize()} with _${word.capitalize()}{"{"}
  const factory {word.capitalize()}() = _{word.capitalize()};
  factory {word.capitalize()}.fromJson(Map<String, dynamic> json) => _${word.capitalize()}FromJson(json);
{"}"}""")
    
    model_body_file_path = os.path.join(model_dir, f"{word}_body.dart")
    if not os.path.exists(model_body_file_path):
        with open(model_body_file_path, "w") as file:
            file.write(f"""
import 'package:freezed_annotation/freezed_annotation.dart';
part '{word}_body.g.dart';
part '{word}_body.freezed.dart';

@freezed
class {word.capitalize()}Body with _${word.capitalize()}Body{"{"}
  const factory {word.capitalize()}Body() = _{word.capitalize()}Body;
  factory {word.capitalize()}Body.fromJson(Map<String, dynamic> json) => _${word.capitalize()}BodyFromJson(json);
{"}"}""")
    
    # Create the view directory
    view_dir = os.path.join(word, "view")
    if not os.path.exists(view_dir):
        os.makedirs(view_dir)
    
    # Create the screens directory inside the view directory
    screens_dir = os.path.join(view_dir, "screens")
    if not os.path.exists(screens_dir):
        os.makedirs(screens_dir)
    
    # Create the widgets directory inside the view directory
    widgets_dir = os.path.join(view_dir, "widgets")
    if not os.path.exists(widgets_dir):
        os.makedirs(widgets_dir)
    
    # Create the data directory
    data_dir = os.path.join(word, "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Create the controller directory
    controller_dir = os.path.join(data_dir, "controller")
    if not os.path.exists(controller_dir):
        os.makedirs(controller_dir)

    # Create the repository directory
    repository_dir = os.path.join(data_dir, "repository")
    if not os.path.exists(repository_dir):
        os.makedirs(repository_dir)
    
    # Create the web_services directory
    web_services_dir = os.path.join(data_dir, "web_services")
    if not os.path.exists(web_services_dir):
        os.makedirs(web_services_dir)
    
    # Generate web services code
    web_services_file_path = os.path.join(web_services_dir, f"{word}_web_services.dart")
    if not os.path.exists(web_services_file_path):
        with open(web_services_file_path, "w") as file:
            file.write(generate_web_services_code(word))
    
    # Generate Flutter screen code
    flutter_screen_file_path = os.path.join(screens_dir, f"{word}_screen.dart")
    if not os.path.exists(flutter_screen_file_path):
        with open(flutter_screen_file_path, "w") as file:
            file.write(generate_flutter_screen(word))
    
    # Generate repository code
    repository_file_path = os.path.join(repository_dir, f"{word}_repository.dart")
    if not os.path.exists(repository_file_path):
        with open(repository_file_path, "w") as file:
            file.write(generate_repository_code(word))
    
    # Generate Cubit code
    cubit_file_path = os.path.join(controller_dir, f"{word}_cubit.dart")
    if not os.path.exists(cubit_file_path):
        with open(cubit_file_path, "w") as file:
            file.write(generate_cubit_code(word))
    
    # Generate state code
    state_file_path = os.path.join(controller_dir, f"{word}_state.dart")
    if not os.path.exists(state_file_path):
        with open(state_file_path, "w") as file:
            file.write(generate_cubit_state_code(word))
main()
