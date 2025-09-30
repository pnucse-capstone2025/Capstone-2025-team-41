import { IsEmail, IsString, MinLength } from 'class-validator';

export class SignupDto {
  @IsEmail() email: string;
  @IsString() @MinLength(8) password: string;
}

export class LoginDto {
  @IsEmail() email: string;
  @IsString() password: string;
}
